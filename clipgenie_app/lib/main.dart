import 'package:flutter/material.dart';
import 'api_service.dart';

void main() => runApp(MaterialApp(home: ScriptGeneratorPage()));

class ScriptGeneratorPage extends StatefulWidget {
  @override
  _ScriptGeneratorPageState createState() => _ScriptGeneratorPageState();
}

class _ScriptGeneratorPageState extends State<ScriptGeneratorPage> {
  final TextEditingController _controller = TextEditingController();
  final ApiService _apiService = ApiService();
  String _script = "";
  bool _isLoading = false;

  void _generate() async {
    setState(() => _isLoading = true);
    final result = await _apiService.generateScript(_controller.text);
    setState(() {
      _script = result ?? "Error occured";
      _isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("ClipGenieAI Script Generator")),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(controller: _controller, decoration: InputDecoration(hintText: "Enter topic...")),
            SizedBox(height: 20),
            _isLoading ? CircularProgressIndicator() : ElevatedButton(onPressed: _generate, child: Text("Generate")),
            Expanded(child: SingleChildScrollView(child: Text(_script))),
          ],
        ),
      ),
    );
  }
}