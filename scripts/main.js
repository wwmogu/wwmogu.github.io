const commandInput = document.getElementById("command-input");
const terminalContent = document.getElementById("terminal-content");
const prompt = document.querySelector(".prompt");

let currentDirectory = "home";

commandInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    e.preventDefault();
    const command = commandInput.value.trim();

    if (command.startsWith("cd ")) {
      const targetDirectory = command.substring(3).trim();

      if (targetDirectory === "blog") {
        currentDirectory = "blog";
        updatePrompt();
        terminalContent.appendChild(createOutputLine(`Navigated to 'blog' directory.`));
      } else if (targetDirectory === "home") {
        currentDirectory = "home";
        updatePrompt();
        terminalContent.appendChild(createOutputLine(`Navigated to 'home' directory.`));
      } else {
        terminalContent.appendChild(createOutputLine(`Directory '${targetDirectory}' not found.`));
      }
    } else if (command === "ls") {
      if (currentDirectory === "home") {
        terminalContent.appendChild(createOutputLine("blog"));
      } else if (currentDirectory === "blog") {
        terminalContent.appendChild(createOutputLine("blog1.md"));
        terminalContent.appendChild(createOutputLine("blog2.md"));
        terminalContent.appendChild(createOutputLine("blog3.md"));
      }
    } else {
      terminalContent.appendChild(createOutputLine(`Command '${command}' not found.`));
    }

    commandInput.value = "";
    commandInput.scrollIntoView();
  }
});

function createOutputLine(text) {
  const outputLine = document.createElement("p");
  outputLine.textContent = text;
  return outputLine;
}

function updatePrompt() {
  if (currentDirectory === "home") {
    prompt.textContent = "wwmogu@adelaide:~$";
  } else if (currentDirectory === "blog") {
    prompt.textContent = "wwmogu@adelaide:blog$";
  }
}

updatePrompt();
