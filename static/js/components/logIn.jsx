import React from 'react'
import axios from 'axios'

class logInForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
      sessionID: ''
    };

    this.handleUsername = this.handleUsername.bind(this);
    this.handlePassword = this.handlePassword.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleUsername(event) {
    this.setState({username: event.target.value});
  }

  handlePassword(event) {
    this.setState({password: event.target.value})
  }

  handleSubmit(event) {

    const data = {
      'username' : this.state.username,
      'password' : this.state.password
    }
    console.log(data)
    axios.post('/login-db', data)
    .then(response => {
      if (response.data) {
        localStorage.setItem('sessionID', response.data)
      }
    })
    event.preventDefault();
    console.log(localStorage.getItem('sessionID'))
    
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
            <label className={'pull-left'}>
              Password
              <input className={'form-control mr-sm-2'} type="text" value={this.state.password} onChange={this.handlePassword} />
            </label>
          </div>
          <input className={'btn btn-outline-success my-2 my-sm-0'}type="submit" value="Login" />
        </form>
      </div>
    );
  }
}

export default logInForm