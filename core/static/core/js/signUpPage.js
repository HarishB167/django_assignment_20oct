$(document).ready(function () {
  console.log("JS loaded - ready.");
});

const doctorApiEndpoint = "/api/doctor/";
const patientApiEndpoint = "/api/patient/";

const schema = {
  username: Joi.string().required().label("Username"),
  first_name: Joi.string().required().label("First name"),
  last_name: Joi.string().required().label("Last name"),
  email: Joi.string().email().max(256).required(),
  password: Joi.string().min(5).required().label("Password"),
  confirm_password: Joi.any()
    .equal(Joi.ref("password"))
    .required()
    .label("Confirm password")
    .options({ language: { any: { allowOnly: "must match password" } } }),
  profile_picture: Joi.optional(),
  address_line1: Joi.string().required().label("Address line"),
  address_city: Joi.string().required().label("City"),
  address_state: Joi.string().required().label("State"),
  address_pincode: Joi.string().required().label("Pin code"),
};

const inputToValidationMessage = {
  username: "#usernameHelp",
  first_name: "#firstNameHelp",
  last_name: "#lastNameHelp",
  email: "#emailAddressHelp",
  password: "#password1Help",
  confirm_password: "#password2Help",
  profile_picture: "#profilePictureHelp",
  address_line1: "#addressLine1Help",
  address_city: "#addressCityHelp",
  address_state: "#addressStateHelp",
  address_pincode: "#addressPinCodeHelp",
};

function displayErrors(error) {
  for (const [key, value] of Object.entries(inputToValidationMessage)) {
    const result = error.details.find((item) => item.path[0] === key);
    if (result)
      $(value).html(result.message).removeClass("hidden").addClass("error");
    else $(value).html("").addClass("hidden").removeClass("error");
  }
}

function doValidation(data) {
  console.log("data :>> ", data);
  const result = Joi.validate(data, schema, {
    abortEarly: false,
  });

  console.log("result :>> ", result);
  if (result.error) {
    displayErrors(result.error);
    return false;
  } else return true;
}

function doSignUp(accountType, data) {
  let endPoint = "";
  if (accountType === "patient") endPoint = patientApiEndpoint;
  else if (accountType == "doctor") endPoint = doctorApiEndpoint;
  else {
    alert("Invalid account type");
    return;
  }

  const formData = new FormData();
  Object.keys(data).forEach((key) => formData.append(key, data[key]));
  formData.append(
    "profile_picture",
    document.querySelector("#profilePicture").files[0]
  );
  axios
    .post(endPoint, formData, {
      headers: { "Content-Type": "multipart/form-data" },
    })
    .then(function (response) {
      console.log("response :>> ", response);
      $("#signUpForm").trigger("reset");
    })
    .catch(function (error) {
      console.log("error :>> ", error);
    });
}

$(document).ready(function () {
  $("#submitForm").click(function (e) {
    e.preventDefault();

    const accountType = $("#accountType").val();
    const firstName = $("#firstName").val();
    const lastName = $("#lastName").val();
    const profilePicture = $("#profilePicture").val();
    const username = $("#username").val();
    const emailAddress = $("#emailAddress").val();
    const password1 = $("#password1").val();
    const password2 = $("#password2").val();
    const addressLine1 = $("#line1").val();
    const addressCity = $("#city").val();
    const addressState = $("#state").val();
    const addressPinCode = $("#pincode").val();

    const data = {
      username: username,
      first_name: firstName,
      last_name: lastName,
      email: emailAddress,
      password: password1,
      confirm_password: password2,
      profile_picture: profilePicture,
      address_line1: addressLine1,
      address_city: addressCity,
      address_state: addressState,
      address_pincode: addressPinCode,
    };

    // const val = `${accountType} ${firstName} ${lastName} ${profilePicture} ${username} ${emailAddress} ${password1} ${password2} ${addressLine1} ${addressCity} ${addressState} ${addressPinCode}`;
    // alert(val);
    if (doValidation(data)) doSignUp(accountType, data);
  });
});
