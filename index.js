class Weighted {
  constructor(gradeRaw, credit, weight) {
    this.gradeRaw = gradeRaw;
    this.credit = credit;
    this.weight = weight;
  }
  addWeight() {
    if (this.gradeRaw !== 0) {
      if (this.weight === "Honors") {
        this.gradeRaw += 1;
      } else if (this.weight === "AP") {
        this.gradeRaw += 2;
      }
    }
  }
  getGradePoint() {
    if (this.gradeRaw === 14) {
      this.GP = 5;
    } else if (this.gradeRaw === 13) {
      this.GP = 4.67;
    } else if (this.gradeRaw === 12) {
      this.GP = 4.33;
    } else if (this.gradeRaw === 11) {
      this.GP = 4;
    } else if (this.gradeRaw === 10) {
      this.GP = 3.67;
    } else if (this.gradeRaw === 9) {
      this.GP = 3.33;
    } else if (this.gradeRaw === 8) {
      this.GP = 3;
    } else if (this.gradeRaw === 7) {
      this.GP = 2.67;
    } else if (this.gradeRaw === 6) {
      this.GP = 2.33;
    } else if (this.gradeRaw === 5) {
      this.GP = 2;
    } else if (this.gradeRaw === 4) {
      this.GP = 1.67;
    } else if (this.gradeRaw === 3) {
      this.GP = 1.33;
    } else if (this.gradeRaw === 2) {
      this.GP = 1.00;
    } else if (this.gradeRaw === 1) {
      this.GP = 0.67;
    } else {
      this.GP = 0;
    }
  }
  GPtimesCredits(credit) {
    this.gradePoint = this.GP * credit;
    return this.gradePoint;
  }
}

class Unweighted {
  constructor(uGP, credit) {
    this.credit = credit;
    this.uGP = uGP;
  }
  GPtimesCredits(credit) {
    this.gradePoint = this.uGP * credit;
    return this.gradePoint;
  }
}

class Ready {
  constructor(isGrade, isWeight, isCredit) {
    this.grade = isGrade;
    this.weight = isWeight;
    this.credits = isCredit;
    this.isCalculated = false;
  }

  setGrade() {
    this.grade = true;
  }

  setWeight() {
    this.weight = true;
  }

  setCredits() {
    this.credits = true;
  }

  isReady() {
    return this.grade && this.weight && this.credits;
  }

  setCalculated() {
    this.isCalculated = true;
  }

  reset() {
    this.grade = false;
    this.weight = false;
    this.credits = false;
  }
}

function promptUser() {
  numCourses += 1;
  instructionText.innerHTML = "Class #" + numCourses + ": ";
  instructionText.innerHTML += " Use the buttons to the Weight -'AP', 'Honors', 'Normal'- of your course, number of credits, and letter grade.";
  instructionText.innerHTML += " If you are done entering information for that course, press DONE to move on.";
  instructionText.innerHTML += " Or, if you finished entering all your classes, press CALCULATE GPA. ";
  userFeedback.innerHTML = "Your entries for this class: "
}

function calculateGPA() {
  if (canMoveOn.isReady() && !calculated) {
    userInput.innerHTML = "";
    creditsAggregation += courseCredits;
    let c_weighted = new Weighted(courseRaw, courseCredits, courseWeight);
    c_weighted.addWeight();
    c_weighted.getGradePoint();
    c_weighted.GPtimesCredits(courseCredits);
    wGradePointList.push(c_weighted.gradePoint);
    let c_unweighted = new Unweighted(uGP, courseCredits);
    c_unweighted.GPtimesCredits(courseCredits);
    gradePointList.push(c_unweighted.gradePoint);
    let wGradePointSum = 0.0;
    let uGradePointSum = 0.0;
    for (let i = 0; i < wGradePointList.length; i++) {
      wGradePointSum += wGradePointList[i];
    }
    let wGPA = wGradePointSum / creditsAggregation;
    wGPA = Math.round(wGPA * 100) / 100;
    for (let i = 0; i < numCourses; i++) {
      uGradePointSum += gradePointList[i];
    }
    let uGPA = uGradePointSum / creditsAggregation;
    uGPA = Math.round(uGPA * 100) / 100;
    instructionText.innerHTML = "";
    display.innerHTML = "Weighted GPA: " + wGPA + ". Unweighted GPA: " + uGPA;
    instructionText.innerHTML = "GPA Calculated. ";
    instructionText.innerHTML += "Weighted GPA: " + wGPA + ". Unweighted GPA: " + uGPA;
    instructionText.innerHTML += "  Press Restart to start again.";
    userFeedback.innerHTML = "";
    calculated = true;
  }
}

function grader(gradeDisp, wGradeRaw, uGradePoint) {
  // Don't do anything with the grade, credit, or weight adder if the GPA is calculated 
  // and the restart button has not been pressed
  if (!calculated) {
    userInput.innerHTML += "Grade: " + gradeDisp + "     ";
    courseRaw = wGradeRaw;
    uGP = uGradePoint;
    canMoveOn.setGrade();
  }
}

function crediter(credit) {
  if (!calculated) {
    userInput.innerHTML += "Credits: " + credit + "      ";
    courseCredits = credit;
    canMoveOn.setCredits();
  }
}

function weighter(weight) {
  if (!calculated) {
    userInput.innerHTML += "Weight: " + weight + "      ";
    courseWeight = weight;
    canMoveOn.setWeight();
  }
}

function storeData() {
  if (canMoveOn.isReady() && !calculated) {
    creditsAggregation += courseCredits;
    c_weighted = new Weighted(courseRaw, courseCredits, courseWeight);
    c_weighted.addWeight();
    c_weighted.getGradePoint();
    c_weighted.GPtimesCredits(courseCredits);
    wGradePointList.push(c_weighted.gradePoint);
    c_unweighted = new Unweighted(uGP, courseCredits);
    c_unweighted.GPtimesCredits(courseCredits);
    gradePointList.push(c_unweighted.gradePoint);
    c_weighted = null;
    c_unweighted = null;
    canMoveOn.reset();
    userInput.innerHTML = "";
    promptUser();
  } else {
    instructionText += " You must click all required buttons before moving on.";
  }
}

function restart() {
  if (canMoveOn.isCalculated) {
    c_weighted = null;
    c_unweighted = null;
  }
  canMoveOn.reset();
  userInput.innerHTML = "";
  userFeedback.innerHTML = "";
  display.innerHTML = "";
  wGradePointList = [];
  gradePointList = [];
  creditsAggregation = 0;
  numCourses = 0;
  courseCredits = 0;
  courseWeight = "null";
  courseRaw = 0;
  uGP = 0.0;
  calculated = false;
  promptUser();
}

const instructionText = document.querySelector("#instructionText");
const userInput = document.querySelector("#userInput");
userInput.innerHTML = "";
const userFeedback = document.querySelector("#userFeedback");
userFeedback.textContent = "";
const display = document.querySelector("#display");

// Calculation variables
let c_weighted;
let c_unweighted;

// Main stuff
let wGradePointList = []
let gradePointList = []
let creditsAggregation = 0;
let numCourses = 0;
let courseCredits = 0.0;
let courseWeight = "null";
let courseRaw = 0;
let uGP;
uGP = 0.0;
let canMoveOn = new Ready(false, false, false)
let calculated = false;

promptUser();