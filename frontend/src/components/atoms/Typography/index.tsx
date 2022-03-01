import React from 'react';
import { StyledTypography } from './styles';

interface TypographyProps {
    children: React.ReactNode;
    variant: 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6' | 'p' | 'span';
    color?: 'main' | 'dark' | 'light';
    size?: 'small' | 'medium' | 'large';
}

const Typography: React.FC<TypographyProps> = ({ children, variant, size = "medium", color = "light" }) => {
    return (
        <StyledTypography as={variant} size={size} color={color}>
            {children}
        </StyledTypography >
    )
}

export default Typography;
