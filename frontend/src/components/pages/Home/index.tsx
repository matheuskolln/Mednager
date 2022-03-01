import React from 'react';
import { Typography } from '../../atoms';
import { Button, ButtonsContainer, Container, ItemsContainer } from './styles';


const Home: React.FC = () => {
  return (
    <Container>
      <ItemsContainer>
        <Typography variant="h1" color="main" size='large'>
          Mednager
        </Typography>
        <Typography variant='p' color="dark" size="medium">
          Welcome to Mednager
        </Typography>
        <ButtonsContainer>
          <Button>Login</Button>
          <Button>Register</Button>
        </ButtonsContainer>
      </ItemsContainer>
    </Container >
  )
}

export default Home;
