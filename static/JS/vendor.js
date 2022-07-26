


// Gender Dropdown Function

  let btngender = document.querySelector("#btngender");

  let spanGender = document.querySelector("#spanGender");

  let gender_LI = document.querySelectorAll("#gender_LI");

  // Category Dropdown Function

  let btncategory = document.querySelector("#btncategory");

  let spanCategory = document.querySelector("#spanCategory");

  let category_LI = document.querySelectorAll("#category_LI");

  btngender.addEventListener("show.bs.dropdown", function () {
    gender_LI.forEach((e) => {
      e.addEventListener("click", () => {
        spanGender.innerHTML = e.innerHTML;
        
      });
    });
  });

  btncategory.addEventListener("show.bs.dropdown", function () {
    category_LI.forEach((e) => {
      e.addEventListener("click", () => {
        spanCategory.innerHTML = e.innerHTML;
      });
    });
  });


 