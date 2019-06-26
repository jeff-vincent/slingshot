import React from 'react';
import SignUpForm from './signUp'
import LogInForm from './logIn'



class App extends React.Component {
  constructor(props) {
    super(props);

  }
  render() {
    return (
      <div >
        <LogInForm/>
        <SignUpForm/>
    	</div>)
  }
}

export default App;
