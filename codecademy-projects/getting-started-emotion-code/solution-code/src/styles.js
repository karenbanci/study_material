import styled from "@emotion/styled";

import { keyframes } from "@emotion/react";

export const theme = {
  colors: {
    primary: "#03045e",
    secondary: "#caf0f8",
    tertiary: "#023e8a",
    quaternary: "#fff",
  },
  fonts: {
    primary: "helvetica",
  },
  fontSize: {
    primary: "20px",
    secondary: "14px",
  },
};

export const LogoSpin = keyframes`
from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`;

export const CardWrapper = styled.div`
  width: 250px;
  height: 325px;
  background: ${(props) => props.theme.colors.quaternary};
  border-radius: 15px;
  padding-bottom: 5px;
  @media (max-width: 900px) {
    width: 400px;
  }
`;

export const ImageWrapper = styled.img`
  object-fit: cover;
  width: 100%;
  height: 60%;
  border-radius: 15px 15px 0 0;
`;

export const TextWrapper = styled.div`
  padding: 10px;
  height: 50px;
`;

export const TitleWrapper = styled.h2`
  margin: 0;
  font-size: ${(props) => props.theme.fontSize.primary};
`;

export const DescriptionWrapper = styled.h3`
  margin-top: 5px;
  font-size: ${(props) => props.theme.fontSize.secondary};
  color: ${(props) => props.theme.colors.tertiary};
`;

export const ActionsWrapper = styled.div`
  margin-left: 10px;
  padding: 10px 0;
  display: flex;
`;

export const Button = styled.button`
  width: 100%;
  margin-right: 10px;
  margin-top: 4px;
  border: 0;
  border-radius: 15px;
  box-shadow: 0 10px 10px rgba(0, 0, 0, 0.08);
  padding: 10px 0;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.02, 0.01, 0.47, 1);

  &:hover {
    box-shadow: 0 15px 15px rgba(0, 0, 0, 0.16);
  }
`;

export const PrimaryButton = styled(Button)`
  background-color: ${(props) => props.theme.colors.primary};
  color: ${(props) => props.theme.colors.secondary};
`;

export const SecondaryButton = styled(Button)`
  background-color: ${(props) => props.theme.colors.secondary};
  color: ${(props) => props.theme.colors.primary};
`;
