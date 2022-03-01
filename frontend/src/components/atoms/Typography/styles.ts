import styled from "styled-components";

const SIZES = {
    small: "1.5rem",
    medium: "3rem",
    large: "4.5rem"
};

const COLORS ={
    main: "#0044ff",
    dark: "#000000",
    light: "#ffffff"
}

interface TypographyProps {
    size: "small" | "medium" | "large";
    color: "main" | "dark" | "light";
}

export const StyledTypography = styled.div<TypographyProps>`
    font-family: 'Roboto', sans-serif;
    font-size: ${props => SIZES[props.size] };
    color: ${props => COLORS[props.color]};
    margin: 0;
`;
