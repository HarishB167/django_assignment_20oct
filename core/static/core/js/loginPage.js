$(document).ready(function () {
  console.log("JS loaded - ready.");
});

const loginEndpoint = "/auth/jwt/create";

const schema = {
  username: Joi.string().required().label("Username"),
  password: Joi.string().min(5).required().label("Password"),
};

const inputToValidationMessage = {
  username: "#usernameHelp",
  password: "#passwordHelp",
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

function doLogin(data) {
  axios
    .post(loginEndpoint, data)
    .then(function (response) {
      console.log("response :>> ", response);
      $("#loginForm").trigger("reset");
      const accessToken = response.data.access;
      const refreshToken = response.data.refresh;
      Cookies.set("accessToken", accessToken);
      Cookies.set("refreshToken", refreshToken);
    })
    .catch(function (error) {
      console.log("error :>> ", error);
    });
}

$(document).ready(function () {
  $("#submitForm").click(function (e) {
    e.preventDefault();

    const username = $("#username").val();
    const password = $("#password").val();

    const data = {
      username: username,
      password: password,
    };
    if (doValidation(data)) doLogin(data);
  });
});
