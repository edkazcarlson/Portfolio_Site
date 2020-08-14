import React, { Component } from 'react'
import Home from './Pages/MainPage';
import './css/skeleton.css'
import {ThemeProvider, createMuiTheme} from '@material-ui/core/styles'
import {
  HashRouter as Router,
  Switch,
  Route} from 'react-router-dom';
import { Paper } from '@material-ui/core';

export class App extends Component{
	constructor(props){
		super(props);
		this.state = {darkMode: true};
	}

	theme = () => (createMuiTheme({
		palette: {
		  type: "dark"
		}
	}));

	render () {
		return (    
		<ThemeProvider theme = {this.theme()}>
			<Paper style = {{borderRadius: '0px'}} >
				<div className= 'App'>
					<Router /*basename={process.env.PUBLIC_URL}*/>
						<Switch>
							<Route path="/">
								<Home switchTheme = {this.switchTheme} darkModeState  = {this.state.darkMode}/>
							</Route>
						</Switch>
					</Router>
				</div>
			</Paper>
		</ThemeProvider>
	)
  }
}

export default App;
