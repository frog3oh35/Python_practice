import os
import sys
import datetime

# --- 1. os 모듈 : 파일 시스템 및 OS 상호작용 ---

def explore_os_and_filesystem():
    """os 모듈을 사용하여 현재 시스템 및 파일 정보를 확인합니다."""

    print("=" * 50)
    print(" OS 모듈 : 시스템 및 파일 시스템 정보 탐색")
    print("=" * 50)

    # 1.1. 현재 작업 디렉토리 확인 및 변경
    current_dir = os.getcwd()
    print(f"1.1. 현재 작업 디렉토리 (CWD): {current_dir}")

    # 1.2. OS 이름 확인
    print(f"1.2. OS 이름 : {os.name}")

    # 1.3. 시스템의 환경 변수 출력 (예시로 PATH만 출력)
    if 'PATH' in os.environ:
        print(f"1.3. 환경 변수 'PATH' (일부): {os.environ['PATH'][:50]}...")
    else:
        print("1.3. 환경 변수 'PATH'를 찾을 수 없습니다.")
    
    # 1.4. 새 디렉토리 생성 및 삭제
    new_dir = "test_directory_for_study"
    try:
        os.mkdir(new_dir)
        print(f"1.4. 디렉토리 생성 성공: {new_dir}")
        
        # 1.5. 파일 생성 및 쓰기 (경로 결합 사용: os.path.join)
        file_path = os.path.join(new_dir, "test_log.txt")
        with open(file_path, 'w') as f:
            f.write(f"테스트 로그 생성 시간: {datetime.datetime.now()}\n")
            f.write(f"현재 CMD는 {current_dir} 입니다.\n")
        print(f"1.5. 파일 생성 및 쓰기 성공: {file_path}")

        # 1.6. 생성된 파일의 크기 확인
        file_size = os.path.getsize(file_path)
        print(f"1.6. 생성된 파일 크기 (바이트): {file_size}")

    except FileExistsError:
        print(f"1.6. 생성된 파일 크기 (바이트): {file_size}")
    
    finally:
        # 1.7. 정리: 파일 및 디렉토리 삭제
        try:
            if 'file_payh' in locals() and os.path.exists(file_path):
                os.remove(file_path)
                print(f"1.7. 파일 삭제 성공: {file_path}")
            if os.path.exists(new_dir):
                os.rmdir(new_dir)
                print(f"1.7. 디렉토리 삭제 성공: {new_dir}")
        except Exception as e:
            print(f"1.7. 정리 중 오류 발생: {e}")

# --- 2. sys 모듈: 파이썬 인터프리터 및 실행 환경 상호작용 ---

def handle_sys_info_and_arguments():
    """sys 모듈을 사용하여 파이썬 환경 정보 및 실행 인자를 처리합니다."""

    print("\n" + "=" * 50)
    print(" SYS 모듈 : 인터프리터 및 인자 처리")
    print("=" * 50)

    # 2.1. 파이썬 인터프리터 버전 확인
    print(f"2.1. 파이썬 버전 정보: {sys.version.split()[0]}")

    # 2.2. 모듈 검색 경로(PATHONPATH) 확인
    print(f"2.2. 모듈 검색 경로 (sys.path) 개수: {len(sys.path)}")
    print(f" - 주요 경로 예시: {sys.path[0]}") # 첫 번째 경로는 보통 스크립트의 디렉토리

    # 2.3. 명령줄 인자 처리 (sys.argv)
    if len(sys.argv) > 1:
        print(f"2.3. 명령줄 인자 개수: {len(sys.argv)}")
        print(f" - 실행 스크립트 이름: {sys.argv[0]}")
        print(f" - 전달된 인자들: {sys.argv[1:]}")

        # 2.4. 특정 인자 값에 따른 동작 수행 예시
        if "clean" in sys.argv:
            print("2.5. 'clean' 인자가 감지되었습니다. 정리 작업을 시작합니다...")
            # 실제 작업 로직을 여기에 추가 가능
        else:
            print("2.4. 추가 인자가 있지만 특별한 동작은 없습니다.")
    else:
        print("2.3. 명령줄 인자가 없습니다. (실행 스크립트 이름만 존재)")
        print(" 팁: 실행 시 'python system_utility.py argument1 clean'처럼 인자를 넣어보세요.")

    #

if __name__ == "__main__":
    explore_os_and_filesystem()
    handle_sys_info_and_arguments()