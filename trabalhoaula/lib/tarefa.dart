class Tarefa {
  final int id;
  final String descricao;
  bool concluida;

  Tarefa({ required this.descricao, required this.concluida, required this.id});

  factory Tarefa.fromMap(Map<String, dynamic> map) {
    return Tarefa(
      id: map['id'] as int,
      descricao: map['descricao'] as String,
      concluida: map['concluida'] == 1,
    );
  }
  }