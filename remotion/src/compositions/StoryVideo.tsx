import React from "react";
import {
  AbsoluteFill,
  Audio,
  Video,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig
} from "remotion";

type Card = {
  start: number;
  end: number;
  title: string;
  body: string;
};

type Props = {
  title: string;
  subtitle: string;
  cards: Card[];
  heygenVideoSrc: string | null;
  audioSrc: string | null;
};

const clamp = (v: number, min: number, max: number) => Math.min(max, Math.max(min, v));

const AnimatedBackground: React.FC = () => {
  const frame = useCurrentFrame();
  const {width, height} = useVideoConfig();
  const t = frame / 30;
  const shift = Math.sin(t * 0.6) * 120;

  return (
    <AbsoluteFill
      style={{
        background: "radial-gradient(1200px 800px at 20% 20%, #0b2a5a 0%, #071a3a 45%, #050f25 100%)"
      }}
    >
      <div
        style={{
          position: "absolute",
          width: width * 1.2,
          height: height * 0.6,
          left: -width * 0.1 + shift,
          top: height * 0.1,
          background: "linear-gradient(110deg, rgba(64,150,255,0.25), rgba(20,60,140,0.05))",
          filter: "blur(40px)",
          borderRadius: 999
        }}
      />
      <div
        style={{
          position: "absolute",
          width: width * 0.8,
          height: height * 0.4,
          right: -width * 0.2 - shift * 0.6,
          bottom: height * 0.05,
          background: "linear-gradient(140deg, rgba(80,170,255,0.18), rgba(10,25,60,0.02))",
          filter: "blur(35px)",
          borderRadius: 999
        }}
      />
    </AbsoluteFill>
  );
};

const CardView: React.FC<{card: Card}> = ({card}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const inFrame = clamp(frame - card.start, 0, 9999);
  const outFrame = clamp(card.end - frame, 0, 9999);
  const appear = spring({frame: inFrame, fps, config: {damping: 16, mass: 0.7}});
  const disappear = spring({frame: outFrame, fps, config: {damping: 20, mass: 0.8}});
  const opacity = interpolate(disappear, [0, 1], [0, 1]);
  const y = interpolate(appear, [0, 1], [40, 0]);

  return (
    <div
      style={{
        position: "absolute",
        left: 80,
        right: 80,
        bottom: 260,
        padding: "28px 32px",
        borderRadius: 28,
        background: "rgba(10, 25, 55, 0.75)",
        border: "1px solid rgba(120, 190, 255, 0.45)",
        boxShadow: "0 18px 40px rgba(0,0,0,0.45)",
        transform: `translateY(${y}px)`,
        opacity
      }}
    >
      <div style={{fontSize: 42, fontWeight: 700, color: "#d6ecff"}}>{card.title}</div>
      <div style={{marginTop: 8, fontSize: 30, color: "#a7c6f5"}}>{card.body}</div>
    </div>
  );
};

export const StoryVideo: React.FC<Props> = ({
  title,
  subtitle,
  cards,
  heygenVideoSrc,
  audioSrc
}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const headerIn = spring({frame, fps, config: {damping: 18}});
  const headerY = interpolate(headerIn, [0, 1], [-30, 0]);

  return (
    <AbsoluteFill>
      <AnimatedBackground />

      <div
        style={{
          position: "absolute",
          top: 80,
          left: 80,
          right: 80,
          transform: `translateY(${headerY}px)`
        }}
      >
        <div style={{fontSize: 54, fontWeight: 800, color: "#eef6ff"}}>{title}</div>
        <div style={{marginTop: 12, fontSize: 32, color: "#b7d2ff"}}>{subtitle}</div>
      </div>

      <div
        style={{
          position: "absolute",
          top: 360,
          left: 180,
          right: 180,
          height: 980,
          borderRadius: 36,
          border: "2px solid rgba(92, 170, 255, 0.85)",
          boxShadow: "0 0 30px rgba(84,160,255,0.4)",
          overflow: "hidden",
          background: "rgba(5, 12, 30, 0.5)"
        }}
      >
        {heygenVideoSrc ? (
          <Video
            src={staticFile(heygenVideoSrc)}
            style={{width: "100%", height: "100%", objectFit: "cover"}}
          />
        ) : (
          <div
            style={{
              width: "100%",
              height: "100%",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              color: "#7aa9ff",
              fontSize: 28
            }}
          >
            Heygen video bekleniyor
          </div>
        )}
      </div>

      {cards.map((card) => {
        if (frame < card.start || frame > card.end) {
          return null;
        }
        return <CardView key={card.title + card.start} card={card} />;
      })}

      {audioSrc ? <Audio src={staticFile(audioSrc)} /> : null}
    </AbsoluteFill>
  );
};
