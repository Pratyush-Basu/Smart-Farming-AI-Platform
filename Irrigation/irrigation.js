let pump = "OFF";

document.getElementById("autoMode").addEventListener("change", function () {
  const modeText = document.getElementById("modeText");
  if (this.checked) {
    modeText.innerText = "Auto Mode Enabled";
    autoDecision();
  } else {
    modeText.innerText = "Manual Mode Enabled";
  }
});

function pumpOn() {
  pump = "ON";
  document.getElementById("pumpStatus").innerText = pump;
}

function pumpOff() {
  pump = "OFF";
  document.getElementById("pumpStatus").innerText = pump;
}

function autoDecision() {
  const soil = "Low";     // demo value
  const rain = "Expected";

  if (soil === "Low" && rain !== "Expected") {
    pumpOn();
  } else {
    pumpOff();
  }
}
