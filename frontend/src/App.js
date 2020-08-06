import React from 'react';
import './App.css';
import axios from 'axios';


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            mock_data: []
        };
    }

    componentDidMount() {
        axios.get('http://localhost/api/v1/get-data', {
                headers: {'Access-Control-Allow-Origin': '*'}
            }
        ).then(res => {
            this.setState({mock_data: res.data});
        })
    }

    render() {
        return (
            <div className="App">
                <header className="App-header">
                    {this.state.mock_data.map(obj => {
                        return <p>{obj}</p>;
                    })}
                </header>
            </div>
        );
    }

}

export default App;
