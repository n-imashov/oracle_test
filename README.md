Задача №1
Для решения данной задачи, мы можем использовать библиотеку ‘networkx’ для работы с графами в Python, это поможет решить задачу коротким и элегантным способом.


import networkx as nx


def check_relation(net, first, second):
    G = nx.Graph(net)

    return nx.has_path(G, first, second)


if __name__ == '__main__':
    net = [
    
        ("Нурбакыт", "Арслан"), ("Жанар", "Эмир"),
        ("Бегимай", "Улук"), ("Эрнис", "Мырза"),
        ("Талгат", "Айдар"), ("Таалай", "Айнуска"),
        ("Назима", "Айжан"), ("Ислам", "Махабат"),
        ("Нурсултан", "Айжаркын"), ("Элиза", "Алибек")
    ]

    assert check_relation(net, "Нурбакыт", "Айжаркын") is True
    assert check_relation(net, "Элиза", "Эмир") is True
    assert check_relation(net, "Махабат", "Таалай") is False
    assert check_relation(net, "Айнуска", "Ислам") is False
    assert check_relation(net, "Нурсултан", "Бегимай") is True
    assert check_relation(net, "Талгат", "Эрнис") is False
    assert check_relation(net, "Айдар", "Мырза") is True

Этот решение с использованием networkx, проверяет наличие пути между двумя пользователями. Код становится более компактным и понятным.
