/** @jsxImportSource @emotion/react */
import { css, ThemeProvider } from "@emotion/react";
import logo from "./logo.png";
import {
  theme,
  LogoSpin,
  CardWrapper,
  ImageWrapper,
  TextWrapper,
  TitleWrapper,
  DescriptionWrapper,
  ActionsWrapper,
  PrimaryButton,
  SecondaryButton,
} from "./styles";

const hotels = [
  {
    id: 1,
    src: "images/hotel-leisure.jpeg",
    alt: "",
    title: "Hotel Leisure",
    description: "Enjoy world-class shopping in the heart of the city.",
  },
  {
    id: 2,
    src: "images/hotel-paradise.jpeg",
    alt: "",
    title: "Hotel Paradise",
    description: "Enjoy open-air spaces, waterfront dining, and poolside fun.",
  },
  {
    id: 3,
    src: "images/hotel-holiday.jpeg",
    alt: "",
    title: "Hotel Holiday",
    description: "Discover your home away from home.",
  },
];

function App() {
  return (
    <ThemeProvider theme={theme}>
      <main
        css={(theme) => ({
          color: theme.colors.primary,
          background: theme.colors.secondary,
          height: "1200px",
          fontFamily: theme.fonts.primary,
        })}
      >
        <img
          src={logo}
          alt=""
          css={css`
            display: absolute;
            margin-top: 15px;
            margin-left: 15px;
            height: 100px;
            width: 100px;
            animation: ${LogoSpin} 10s linear infinite;
          `}
        />
        <div
          css={css`
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            padding: 20px;
            @media (max-width: 900px) {
              display: grid;
            }
          `}
        >
          {hotels.map((hotel) => {
            return (
              <CardWrapper key={hotel.id}>
                <ImageWrapper src={hotel.src} alt={hotel.alt} />
                <TextWrapper>
                  <TitleWrapper>{hotel.title}</TitleWrapper>
                  <DescriptionWrapper>{hotel.description}</DescriptionWrapper>
                </TextWrapper>
                <ActionsWrapper>
                  <PrimaryButton>Details</PrimaryButton>
                  <SecondaryButton>Book</SecondaryButton>
                </ActionsWrapper>
              </CardWrapper>
            );
          })}
        </div>
      </main>
    </ThemeProvider>
  );
}

export default App;
