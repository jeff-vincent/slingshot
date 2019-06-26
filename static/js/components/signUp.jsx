import React from 'react'
import axios from 'axios'

class SignUpForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
      phoneNumber: '',
    };

    this.handleUsername = this.handleUsername.bind(this)
    this.handlePassword = this.handlePassword.bind(this)
    this.handlePhoneNumber = this.handlePhoneNumber.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handlePhoneNumber(event) {
    this.setState({phoneNumber: event.target.value})
  }

  handleUsername(event) {
    this.setState({username: event.target.value})
  }

  handlePassword(event) {
    this.setState({password: event.target.value})
  }

  handleSubmit(event) {
    const data = {
      'username' : this.state.username,
      'password' : this.state.password,
      'phone_number' : this.state.phoneNumber
    }
    console.log(data)
    axios.post('/signup-db', data)
    .then(response => {
      if (response.data) {
        console.log(response.data)
      }
    })
    event.preventDefault();
  }

  render() {
    return (
      <div className={'navbar navbar-light bg-light'}>
        <form className={'form-inline'} onSubmit={this.handleSubmit}>
          <div className={'form-group'}>
            <label>
              Username
              <input className={'form-control mr-sm-2'} type="text" value={this.state.username} onChange={this.handleUsername} />
            </label>
          </div>
          <div className={'form-group'}>
            <label>
              Password
              <input className={'form-control mr-sm-2'} type="text" value={this.state.password} onChange={this.handlePassword} />
            </label>
          </div>
          <div className={'form-group'}>
            <label>
              Phone Number
              <input className={'form-control mr-sm-2'} type="text" value={this.state.phoneNumber} onChange={this.handlePhoneNumber} />
            </label>
          </div>
          <input className={'btn btn-outline-success my-2 my-sm-0'}type="submit" value="Sign up" />
        </form>
      </div>
    );
  }
}

export default SignUpForm