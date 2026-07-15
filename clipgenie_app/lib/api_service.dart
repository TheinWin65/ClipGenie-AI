import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl = "http://127.0.0.1:8000"; // Backend လိပ်စာ

  Future<String?> generateScript(String topic) async {
    final response = await http.post(
      Uri.parse('$baseUrl/generate-script'),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"topic": topic}),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body)['script'];
    } else {
      return "Error: Could not generate script";
    }
  }
}