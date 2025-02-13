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
}

function promptUser() {
  numCourses += 1;
  canMoveOn = new Ready(false, false, false);
  console.log();
  console.log("Class #" + numCourses + ": ");
  console.log("Use the buttons to enter the grade, number of credits, and Weight -'AP', 'Honors', 'Normal'- of your course.");
  console.log("If you are done entering information for that course, press DONE to move on.");
  console.log("Or, if you finished entering all your classes, press CALCULATE GPA. ");
}

function calculateGPA() {
  if (canMoveOn.isReady()) {
    creditsAggregation += courseCredits;
    let c_weighted = new Weighted(courseRaw, courseCredits, courseWeight);
    c_weighted.addWeight();
    c_weighted.getGradePoint();
    c_weighted.GPtimesCredits(courseCredits);
    wGradePointList.push(c_weighted.gradePoint);
    let c_unweighted = new Unweighted(uGP, courseCredits);
    c_unweighted.GPtimesCredits(courseCredits);
    gradePointList.push(c_unweighted.gradePoint);
    weights.set("");
    credits.set("");
    grades.set("");
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
    console.log();
    console.log("Your weighted GPA is " + wGPA);
    console.log("Your unweighted GPA is " + uGPA);
    disp_Weighted.set(wGPA.toString());
    disp_Unweighted.set(uGPA.toString());
  }
}

function grader(gradeDisp, wGradeRaw, uGradePoint) {
  grades.set(gradeDisp);
  courseRaw = wGradeRaw;
  uGP = uGradePoint;
  canMoveOn.setGrade();
}

function crediter(credit) {
  credits.set(credit);
  courseCredits = credit;
  canMoveOn.setCredits();
}

function weighter(weight) {
  weights.set(weight);
  courseWeight = weight;
  canMoveOn.setWeight();
}



// Main stuff
let wGradePointList = []
let gradePointList = []
let creditsAggregation = 0;
let courseGrade;
let numCourses = 0;
let courseCredits = 0.0;
let courseWeight = null;
let courseRaw = 0;
let uGP;
uGP = 0.0;
console.log("Welcome to the GPA Calculator with TKINTER.")
promptUser()