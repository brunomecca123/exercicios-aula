import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
class DBHelper{
  late Database _database;

  Future<void> inicializarDatabase() async{
    _database = await openDatabase(
      join(await getDatabasesPath(), 'tarefas.db'),
      onCreate: (db, version){
        return db.execute('CREATE TABLE tarefas(id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT, concluida INTEGER)');
      },
      version: 1,
    );
  }

  Future<void> inserirTarefa(Map<String,dynamic> tarefa) async {
    await _database.insert(
      'tarefas',
      tarefa,
      conflictAlgorithm: ConflictAlgorithm.replace,
    );
  }

  Future<void> atualizarTarefa(Map<String,dynamic> tarefa) async {
    await _database.update(
      'tarefas',
      tarefa,
      where: 'id = ?',
      whereArgs: [tarefa['id']],
    );
  }

  Future<void> deletarTarefa(int id) async {
    await _database.delete(
      'tarefas',
      where: 'id = ?',
      whereArgs: [id],
    );
  }

  Future<List<Map<String, dynamic>>> pegarTarefas() async {
    return await _database.query('tarefas');
  }

}