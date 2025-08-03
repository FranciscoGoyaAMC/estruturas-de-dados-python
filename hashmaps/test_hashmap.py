from hashmap import HashMap
from user import get_users


def test_insert_and_get():
    hashmap = HashMap(5)
    user = get_users(1)[0]
    hashmap.insert("user1", user)
    assert hashmap.get("user1") == user


def test_overwrite_key():
    hashmap = HashMap(5)
    user1 = get_users(1)[0]
    user2 = get_users(2)[1]
    hashmap.insert("key", user1)
    hashmap.insert("key", user2)
    assert hashmap.get("key") == user2


def test_key_not_found():
    hashmap = HashMap(5)
    try:
        hashmap.get("missing")
        assert False, "Esperava exceção de chave não encontrada"
    except Exception as e:
        assert str(e) == "sorry, key not found"


def test_collision_linear_probing():
    hashmap = HashMap(3)
    user1 = get_users(1)[0]
    user2 = get_users(2)[1]
    hashmap.insert("abc", user1)
    hashmap.insert("acb", user2)
    assert hashmap.get("abc") == user1
    assert hashmap.get("acb") == user2


def test_resize_works():
    hashmap = HashMap(2)
    users = get_users(10)
    for i, user in enumerate(users):
        hashmap.insert(f"user{i}", user)
    for i, user in enumerate(users):
        assert hashmap.get(f"user{i}") == user
    assert len(hashmap.hashmap) > 2  # houve resize


def test_delete_key():
    hashmap = HashMap(5)
    user = get_users(1)[0]
    hashmap.insert("delete_me", user)
    hashmap.delete("delete_me")
    try:
        hashmap.get("delete_me")
        assert False, "Esperava exceção após delete"
    except Exception as e:
        assert str(e) == "sorry, key not found"


def test_tombstone_does_not_break_probe():
    hashmap = HashMap(5)
    users = get_users(3)
    hashmap.insert("abc", users[0])
    hashmap.insert("acb", users[1])  # colisão com abc
    hashmap.delete("abc")  # cria tombstone
    assert hashmap.get("acb") == users[1]
    hashmap.insert("abc", users[2])  # reutiliza tombstone
    assert hashmap.get("abc") == users[2]


if __name__ == "__main__":
    test_insert_and_get()
    test_overwrite_key()
    test_key_not_found()
    test_collision_linear_probing()
    test_resize_works()
    test_delete_key()
    test_tombstone_does_not_break_probe()
    print("✅ Todos os testes passaram com sucesso!")
