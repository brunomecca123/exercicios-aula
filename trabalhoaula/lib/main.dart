import 'package:flutter/material.dart';
import 'package:trabalhoaula/dbHelper.dart';
import 'package:trabalhoaula/tarefa.dart';

void main() {
  runApp(const ListaDeTarefasApp());
}

class ListaDeTarefasApp extends StatelessWidget {
  const ListaDeTarefasApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Lista de Tarefas App',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const TelaInicial(),
    );
  }
}

class TelaInicial extends StatelessWidget{
  const TelaInicial({super.key});

  @override
  Widget build(BuildContext context){
   
  return Scaffold(
    appBar: AppBar(title: const Text('tela inicial'),),
    body: Center(
      child: ElevatedButton(
        onPressed: (){
          Navigator.of(context).push(
            MaterialPageRoute(
              builder: (context) => const ListaDeTarefasScreen(),)
          );
        },
        child: const Text('Iniciar uma lista de tarefas'),
      ),
    )
  );
}
}

class ListaDeTarefasScreen extends StatefulWidget {
  const ListaDeTarefasScreen({super.key});


  @override
  ListaDeTarefasScreenState createState() => ListaDeTarefasScreenState();
}

class ListaDeTarefasScreenState extends State<ListaDeTarefasScreen> {
  final List<Tarefa> _tarefas = [];
  final TextEditingController _controller = TextEditingController();
  final DBHelper dbHelper = DBHelper();

  @override
  void initState(){
    super.initState();
    dbHelper.inicializarDatabase().then((_){
      _carregarTarefas();
    });
  }

  Future<void> _carregarTarefas() async {
    final tarefas = await dbHelper.pegarTarefas();
    _tarefas.clear();
    _tarefas.addAll(
      tarefas.map((map) => Tarefa.fromMap(map),
    ),
    );
  }

  Future<void> _adicionarTarefa(String descricao) async {
   
      final novaTarefa = {'descricao': descricao, 'concluida': 0};
      await dbHelper.inserirTarefa(novaTarefa);
      _controller.clear();
      _carregarTarefas();
    
  }

  void _removerTarefa(int index) {
    setState(() {
      _tarefas.removeAt(index);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Lista de Tarefas')),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: _tarefas.length,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text(_tarefas[index].descricao),
                  leading: Checkbox(
                    value: _tarefas[index].concluida,
                    onChanged: (bool? newValue) {
                      setState(() {
                        _tarefas[index].concluida = newValue ?? false;
                     });
                    },
                  ),
                    trailing: IconButton(
                      onPressed: (){
                      _removerTarefa(index);
                   },
                    icon: const Icon(Icons.delete)
                    )
                  );
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    onSubmitted: (descricao) {
                      _adicionarTarefa(descricao);
                    },
                    decoration: const InputDecoration(
                      hintText: 'Adicionar Tarefa',
                    ),
                  ),
                ),
                ElevatedButton(
                  child: const Text('Adicionar'),
                  onPressed: (){
                    if(_controller.text.isNotEmpty){
                      _adicionarTarefa(_controller.text);
                    }
                  }, )
              ],
            ),
          ),
        ],
      ),
    );
  }
}