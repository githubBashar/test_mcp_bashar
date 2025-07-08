# GitHub MCP Server Setup

Dieses Repository enthält eine Konfigurationsdatei für den lokalen Betrieb eines GitHub MCP-Servers mit Docker.

## Voraussetzungen

- **Docker**: Stellen Sie sicher, dass Docker auf Ihrem System installiert und konfiguriert ist.
- **GitHub Personal Access Token**: Ein gültiges Token mit den erforderlichen Berechtigungen.

## Konfiguration

Die Konfigurationsdatei befindet sich unter `.vscode/mcp.json` und enthält die folgenden Einstellungen:

```jsonc
{
  "servers": {
    "github-mcp-local": {
      "type": "stdio",
      "command": "docker",
      "args": [
        "run",
        "-i",  // wichtig: damit stdio offen bleibt
        "-e", "GITHUB_PERSONAL_ACCESS_TOKEN=<Ihr-Token>",
        "ghcr.io/github/github-mcp-server:latest",
        "stdio"
      ]
    }
  }
}
```

### Wichtige Hinweise
- **Token-Sicherheit**: Speichern Sie Ihr GitHub Personal Access Token nicht direkt in der Konfigurationsdatei. Nutzen Sie stattdessen Umgebungsvariablen oder einen sicheren Speicher.
- **Docker-Image**: Das verwendete Docker-Image ist `ghcr.io/github/github-mcp-server:latest`. Stellen Sie sicher, dass Sie Zugriff darauf haben.

## Starten des Servers

1. Öffnen Sie Visual Studio Code.
2. Stellen Sie sicher, dass die `.vscode/mcp.json`-Datei korrekt konfiguriert ist.
3. Starten Sie den Server über die Befehlspalette:
   - **MCP: Server auflisten**
   - Wählen Sie `github-mcp-local` aus der Liste aus.

## Fehlerbehebung

- **401 Unauthorized**: Stellen Sie sicher, dass das GitHub Personal Access Token gültig ist und die erforderlichen Berechtigungen besitzt.
- **Docker-Probleme**: Überprüfen Sie, ob Docker korrekt installiert und ausgeführt wird.

## Lizenz

Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).

## Dateien im Repository

- **hallo.txt**: Eine einfache Textdatei mit der Nachricht "hallo bashar".
- **hello_world.py**: Ein Python-Skript, das die Nachricht "Hello, World!!" ausgibt.
- **mcp_server_github.txt**: Eine Beschreibung eines MCP-Servers und dessen Nutzung.