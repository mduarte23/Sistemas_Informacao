import React, {Component} from 'react';
export default class App extends Component {
    state = {
        data: [],
    }
    // metodo executado depois que o componente é montado
    componentDidMount() {
        fetch ('https://holidayapi.com/v1/holidays?pretty&key=098af81c-0cb5-47f7-9d01-97ef27b9859e&country=BR&year=2024&language=pt')
        .then((result) => result.json())
        .then((result) => {
            this.setState({
                data: result.holidays,
            })
        })
    }

    render() {
        const result = this.state.data.map((entry, index) => {
            // return <li key={index}>{entry.name}</li>
            return <option value={index}>{entry.name} | {entry.date}</option>
        })

        // return <ul>{result}</ul>
        return <select>{result}</select>

        // Alterar o codigo para mostrar todos os Pokemons em um campo select
    }
}