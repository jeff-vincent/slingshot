import React from 'react';

class Controls extends React.Component {
 constructor(props) {
   super(props);

   this.signUp = this.signUp.bind(this);
   this.logIn = this.logIn.bind(this);
   this.deleteUser = this.deleteUser.bind(this);
   this.askQuestion = this.askQuestion.bind(this);
   this.setAnswer = this.setAnswer.bind(this)
   this.setUsername = this.setUsername.bind(this)
   this.setPassword = this.setPassword.bind(this)
   this.setPhone = this.setPhone.bind(this)
   this.setQuestion = this.setQuestion.bind(this)


   this.state = {
     username:'',
     password:'',
     phoneNumber:'',
     question:'',
     correctAnswer:'',
     sessionID:'',
   }
 }

 setUsername() {
   this.setState({username : event.target.value})
 }

 setPassword() {
   this.setState({password : event.target.value})
 }

 setPhone() {
   this.setState({phoneNumber : event.target.value})
 }

 setQuestion() {
   this.setState({question : event.target.value})
 }

 setAnswer() {
   this.setState({correctAnswer : event.target.value})
 }

 signUp() {

    fetch('http://0.0.0.0:5000/signup-db/', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: this.state.username,
        password: this.state.password,
      })
    })
    .then((response) => setState({signUp : 'Success.'}))
 }
 
 logIn() {
   return
 }

 deleteUser() {
   return
 }

 askQuestion() {
   return
 }

 render() {
   return (
     <div id="controls" className="row height400 bg-lt-gry rounded-corners blk-border">
       <div className="six columns rounded-corners ">
         <input id="userName" onChange={this.setUsername} type={Text}>Username</input>
         <input id="passWord" onChange={this.setPassword} type={Text}>Password</input>
         <input id="phoneNumber" onChange={this.setPhone} type={Text}>Twilio Generated Phone Number</input>
         <button className="button" onclick={this.signUp}> Sign Up </button>
         <button className="button" onclick={this.logIn}> Login </button>
         <h1>----------------------------------------------------------</h1>
         <h3>Delete 'choSelf by entering your username and password, and then clicking below.</h3>
         <button className="button" onclick={this.deleteUser}> Delete User </button>
         <h1>----------------------------------------------------------</h1>
         <button className="button" onclick={this.askQuestion}> Ask Question </button>
         <input id="userName" onChange={this.setQuestion} type={Text}>Question</input>
         <input id="passWord" onChange={this.setAnswer} type={Text}>Correct Answer</input>
     </div>
    </div>
   );
 }
}

export default Controls
