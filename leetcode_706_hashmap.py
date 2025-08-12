class MyHashMap(object):

    def __init__(self):
        # 버킷 개수
        self.M = 1009
        # 각 칸이 리스트(체이닝), 각 원소는 tuple 형태로 저장
        self.buckets = [[] for _ in range(self.M)]
    
    def _hash(self, key):
        # key를 M으로 나눈 나머지
        return key % self.M

    def put(self, key, value):
        idx = self._hash(key)
        bucket = self.buckets[idx]

        # 같은 key가 이미 있으면 덮어쓰기 (update)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # 없으면 새로 추가
        bucket.append((key, value))

    def get(self, key):
        idx = self._hash(key)
        bucket = self.buckets[idx]

        # 해당 key를 찾아서 삭제
        for (k, v) in bucket:
            if k == key:
                return v
        return -1 # 없으면 -1

    def remove(self, key):
        idx = self._hash(key)
        bucket = self.buckets[idx]

        # 해당 key를 찾아서 삭제
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # i 번째 원소 제거
                bucket.pop(i)
                return