import sys
from pathlib import Path

# 프로젝트 루트를 파이썬 경로에 추가하여 `app` 패키지 임포트 오류 방지
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel

from app.main import create_app
from app.db.session import engine as app_engine


@pytest.fixture(scope="session")
def real_engine():
	# 앱이 사용하는 실제 엔진에 테이블 보장
	SQLModel.metadata.create_all(app_engine)
	return app_engine


@pytest.fixture()
def app_real():
	# 의존성 오버라이드 없이 실제 DB 세션을 사용하도록 앱 인스턴스 생성
	return create_app()


@pytest.fixture()
def client_real(app_real) -> Generator[TestClient, None, None]:
	with TestClient(app_real) as c:
		yield c


