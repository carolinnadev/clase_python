const expressionDisplay = document.querySelector("#expression");
const resultDisplay = document.querySelector("#result");
let expression = "";
let resultWasShown = false;

function render(value = "0", hint = "") {
  expressionDisplay.textContent = hint || (expression
    ? expression.replaceAll("*", "×").replaceAll("/", "÷").replaceAll("-", "−")
    : "Listo para calcular");
  resultDisplay.textContent = value;
}

function appendNumber(number) {
  if (resultWasShown) {
    expression = "";
    resultWasShown = false;
  }
  expression += number;
  render(expression);
}

function appendOperator(operator) {
  if (resultWasShown) resultWasShown = false;
  if (!expression && operator !== "-") return;
  if (/[+\-*/^]$/.test(expression)) {
    expression = expression.slice(0, -1) + operator;
  } else {
    expression += operator;
  }
  render(resultDisplay.textContent);
}

function appendDecimal() {
  if (resultWasShown) {
    expression = "";
    resultWasShown = false;
  }
  const currentNumber = expression.split(/[+\-*/^()]/).at(-1);
  if (!currentNumber.includes(".")) {
    expression += currentNumber ? "." : "0.";
  }
  render(expression);
}

function appendPercent() {
  if (resultWasShown) resultWasShown = false;
  if (expression && !expression.endsWith("%")) expression += "%";
  render(expression || "0");
}

function applyFunction(name) {
  if (resultWasShown) resultWasShown = false;
  const trailingNumber = expression.match(/(?:\d+\.?\d*|\.\d+)$/);
  if (trailingNumber) {
    const start = trailingNumber.index;
    expression = expression.slice(0, start) + `${name}(${trailingNumber[0]})`;
  } else {
    expression += `${name}(`;
  }
  render(resultDisplay.textContent);
  expressionDisplay.textContent = expression
    .replaceAll("sqrt", "√")
    .replaceAll("cbrt", "∛")
    .replaceAll("*", "×")
    .replaceAll("/", "÷")
    .replaceAll("-", "−");
}

function tokenize(source) {
  const tokens = source.match(/(?:\d+\.?\d*|\.\d+)|sqrt|cbrt|log|sin|tan|[()+\-*/^%]/g);
  if (!tokens || tokens.join("") !== source.replace(/\s/g, "")) {
    throw new Error("Expresión no válida");
  }
  return tokens;
}

function evaluate(source) {
  const tokens = tokenize(source);
  let position = 0;
  const precedence = { "+": 1, "-": 1, "*": 2, "/": 2, "^": 3 };

  function parsePrefix() {
    const token = tokens[position++];
    if (token === "+") return parseExpression(4);
    if (token === "-") return -parseExpression(4);
    if (["sqrt", "cbrt", "log", "sin", "tan"].includes(token)) {
      let value;
      if (tokens[position] === "(") {
        position++;
        value = parseExpression(0);
        if (tokens[position] === ")") position++;
      } else {
        value = parsePrefix();
      }
      if (token === "sqrt") return Math.sqrt(value);
      if (token === "cbrt") return Math.cbrt(value);
      if (token === "log") return Math.log10(value);
      if (token === "sin") return Math.sin(value * Math.PI / 180);
      return Math.tan(value * Math.PI / 180);
    }
    if (token === "(") {
      const value = parseExpression(0);
      if (tokens[position] === ")") position++;
      return value;
    }
    const number = Number(token);
    if (!Number.isFinite(number)) throw new Error("Número no válido");
    return number;
  }

  function parseExpression(minimumPrecedence) {
    let left = parsePrefix();
    while (position < tokens.length) {
      const operator = tokens[position];
      if (operator === "%") {
        position++;
        left /= 100;
        continue;
      }
      const operatorPrecedence = precedence[operator];
      if (operatorPrecedence === undefined || operatorPrecedence < minimumPrecedence) break;
      position++;
      const nextMinimum = operator === "^" ? operatorPrecedence : operatorPrecedence + 1;
      const right = parseExpression(nextMinimum);
      if (operator === "+") left += right;
      if (operator === "-") left -= right;
      if (operator === "*") left *= right;
      if (operator === "/") left /= right;
      if (operator === "^") left **= right;
    }
    return left;
  }

  const value = parseExpression(0);
  if (position !== tokens.length || !Number.isFinite(value)) {
    throw new Error("No se puede calcular");
  }
  return value;
}

function calculate() {
  if (!expression || /[+\-*/^.]$/.test(expression)) return;
  try {
    const openParentheses = (expression.match(/\(/g) || []).length;
    const closedParentheses = (expression.match(/\)/g) || []).length;
    const completeExpression = expression + ")".repeat(Math.max(0, openParentheses - closedParentheses));
    const value = evaluate(completeExpression);
    const formatted = Number.parseFloat(value.toPrecision(10)).toString();
    render(formatted, completeExpression
      .replaceAll("sqrt", "√")
      .replaceAll("cbrt", "∛")
      .replaceAll("*", "×")
      .replaceAll("/", "÷")
      .replaceAll("-", "−"));
    expression = formatted;
    resultWasShown = true;
  } catch {
    render("Error", "Revisa la operación");
    resultWasShown = true;
    expression = "";
  }
}

function clearCalculator() {
  expression = "";
  resultWasShown = false;
  render();
}

function deleteLast() {
  if (resultWasShown) return clearCalculator();
  expression = expression.slice(0, -1);
  render(expression || "0");
}

document.querySelector(".keypad").addEventListener("click", (event) => {
  const button = event.target.closest("button");
  if (!button) return;
  if (button.dataset.number !== undefined) appendNumber(button.dataset.number);
  if (button.dataset.operator) appendOperator(button.dataset.operator);
  if (button.dataset.function) applyFunction(button.dataset.function);
  if (button.dataset.action === "decimal") appendDecimal();
  if (button.dataset.action === "percent") appendPercent();
  if (button.dataset.action === "equals") calculate();
  if (button.dataset.action === "clear") clearCalculator();
});

document.addEventListener("keydown", (event) => {
  if (/^[0-9]$/.test(event.key)) appendNumber(event.key);
  else if (["+", "-", "*", "/", "^"].includes(event.key)) appendOperator(event.key);
  else if (event.key === "." || event.key === ",") appendDecimal();
  else if (event.key === "%") appendPercent();
  else if (event.key === "Enter" || event.key === "=") calculate();
  else if (event.key === "Backspace") deleteLast();
  else if (event.key === "Escape") clearCalculator();
  else return;
  event.preventDefault();
});
