# test cases:
# validate('Timmy','password') --> 'Successfully Logged in!'
# validate('Timmy','h4x0r') --> 'Wrong username or password!'
# validate('Alice','alice') --> 'Successfully Logged in!'
# validate('Timmy','password"||""=="') --> 'Wrong username or password!'
# validate('Admin','gs5bw"||1==1//') --> 'Wrong username or password!'

function validate(username, password){
  var database = new Database();
  return database.login(username, password);
}
