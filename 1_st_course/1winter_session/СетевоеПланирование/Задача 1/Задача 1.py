import networkx as nx
import matplotlib.pyplot as plt

# Создаем граф
G = nx.DiGraph()

# Регулируем расположение точек


# Определяем связи между точками
edges_points = {
    'b1(10)': (1, 2),
    'b2(7)': (1, 3),
    'b3(8)': (2, 4),
    'b4(6)': (3, 4),
    'b5(7)': (4, 5),
    'b6(10)': (4, 6),
    'b7(15)': (3, 6),
    'b8(9)': (5, 7),
    'b9(7)': (5, 8),
    'b10(11)': (6, 9),
    'b11(9)': (7, 9)
}

# Определяем связи между рёбрами
edges_edges = [
    ('b1(10)', 'b3(8)'),
    ('b2(7)', 'b4(6)'), ('b2(7)', 'b7(15)'),
    ('b3(8)', 'b5(7)'), ('b3(8)', 'b6(10)'),
    ('b4(6)', 'b5(7)'), ('b4(6)', 'b6(10)'),
    ('b5(7)', 'b8(9)'), ('b5(7)', 'b9(7)'), ('b5(7)', 'b10(11)'),
    ('b6(10)', 'b9(7)'), ('b6(10)', 'b10(11)'),
    ('b7(15)', 'b9(7)'), ('b7(15)', 'b10(11)'),
    ('b8(9)', 'b11(9)'), ('b9(7)', 'b11(9)')
]

weights = {
    'b1(10)': 10,
    'b2(7)': 7,
    'b3(8)': 8,
    'b4(6)': 6,
    'b5(7)': 7,
    'b6(10)': 10,
    'b7(15)': 15,
    'b8(9)': 9,
    'b9(7)': 7,
    'b10(11)': 11,
    'b11(9)': 9
}

# Добавляем вершины и рёбра в граф
for edge, points in edges_points.items():
    G.add_edge(points[0], points[1], label=edge, weight=weights[edge])

pos = {
    1: (10, 40),
    2: (15, 45),
    3: (15, 35),
    4: (20, 45),
    5: (20, 35),
    6: (30, 45),
    7: (30, 35),
    8: (30, 30),
    9: (35, 40)
}

# Визуализируем граф между точками
# pos = nx.spring_layout(G)

labels = nx.get_edge_attributes(G, 'label')
plt.figure(figsize=(10, 7))
nx.draw(
    G, pos, with_labels=True, node_size=350, font_weight='bold'
)


# Рисуем пунктирные ребра отдельно с явным указанием стиля
edges = nx.draw_networkx_edges(G, pos, edgelist=[(5, 6)], style='dashed', arrows=False)
G.add_edge(5, 6, label='0', weight=0)
edges = nx.draw_networkx_edges(G, pos, edgelist=[(8, 7)], style='dashed', arrows=True)
G.add_edge(8, 7, label='1', weight=0)

nx.draw_networkx_edge_labels(G, pos, edge_labels={(6, 5): 0})
nx.draw_networkx_edge_labels(G, pos, edge_labels={(8, 7): 0})

weights['0'] = 0
weights['1'] = 0

plt.title('Граф связей между точками')

# Расчет ранних сроков наступления событий (forward pass)
earliest_start = {node: float('-inf') for node in G}
earliest_start[1] = 0

for node in nx.topological_sort(G):
    for pred in G.predecessors(node):
        earliest_start[node] = max(earliest_start[node], earliest_start[pred] + G.edges[pred, node]['weight'])

# Расчет поздних сроков наступления событий (backward pass)
latest_start = {node: float('inf') for node in G}
latest_start[9] = earliest_start[9]

for node in reversed(list(nx.topological_sort(G))):
    for succ in G.successors(node):
        latest_start[node] = min(latest_start[node], latest_start[succ] - G.edges[node, succ]['weight'])

# Отображение на графе раннних и поздних сроков
for node in G.nodes:
    x, y = pos[node]
    plt.text(x, y + 0.75, 'Ранний: {}'.format(earliest_start[node]), fontsize=9, ha='center',
             bbox=dict(facecolor='black', alpha=0.6, edgecolor='none', boxstyle='round,pad=0.2'), color='white')
    plt.text(x, y - 0.8, 'Поздний: {}'.format(latest_start[node]), fontsize=9, ha='center',
             bbox=dict(facecolor='black', alpha=0.6, edgecolor='none', boxstyle='round,pad=0.2'), color='white')

# Альтернативный вариант добавления весов в ребра на графике
# for edge in G.edges.data():
#     print(edge)
#     x = pos[edge[1]][0] - (pos[edge[1]][0] - pos[edge[0]][0]) / 2
#     y = pos[edge[1]][1] - (pos[edge[1]][1] - pos[edge[0]][1]) / 2
#     plt.text(x, y - 0.65, '{}'.format(weights[edge[2]['label']]), fontsize=9, ha='center',
#              bbox=dict(facecolor='green', alpha=0.6, edgecolor='none', boxstyle='round,pad=0.2'), color='white')

# Определение критического пути
critical_path = []
for node in G.nodes:
    if earliest_start[node] == latest_start[node]:
        critical_path.append(node)

# Помечаем на графе критический путь
for u, v in G.edges:
    if u in critical_path and v in critical_path:
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=2.0, edge_color='green')
# Помечаем на графе названия рёбер
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=labels, font_color='red'
)

# Вычисление резервов времени
total_float = {}
free_float = {}
for u, v in G.edges:
    total_float[(u, v)] = latest_start[v] - earliest_start[u] - G[u][v]['weight']
    free_float[(u, v)] = earliest_start[v] - latest_start[u] - G[u][v]['weight']

# Коэффициенты напряженности некритических дуг
tension_coeff = {
    edge: free_float[edge] / total_float[edge] if total_float[edge] != 0 else float('inf') for edge in total_float
}

print("Ранние сроки:", earliest_start)
sorted_keys = sorted(latest_start.keys(), reverse=True)
print("Поздние сроки: {", end='')
for key in sorted_keys:
    print(key, ": ", str(latest_start[key]) + ', ' if latest_start[key] > 0 else str(latest_start[key]) + '}', end='', sep='')
print("\nКритический путь:", critical_path)
print("Полные резервы:", total_float)
print("Независимые резервы:", free_float)
print("Коэффициенты напряженности некритических дуг:", {k: v for k, v in tension_coeff.items() if v!= float('inf')})

plt.show()
