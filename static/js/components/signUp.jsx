import React from 'react'

class NameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: ''
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
    console.log('Username: ' + this.state.username + 'Password: ' + this.state.password);
    event.preventDefault();
  }

  render() {
    return (
        <form  className={'jumbotron'} onSubmit={this.handleSubmit}>
          <label>
            username:
            <input type="text" value={this.state.username} onChange={this.handleUsername} />
          </label>
          <label>
            password:
            <input type="text" value={this.state.password} onChange={this.handlePassword} />
          </label>
          <input  type="submit" value="Sign up" />
        </form>
    );
  }
}

export default NameForm