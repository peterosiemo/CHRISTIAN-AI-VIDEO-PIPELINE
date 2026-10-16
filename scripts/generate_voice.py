
import argparse
import asyncio
from pathlib import Path

import edge_tts


async def generate_voice(text: str, voice: str, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)

    speech = edge_tts.Communicate(text, voice)
    await speech.save(str(output))

    print(f"Audio saved successfully: {output.resolve()}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate devotional narration using Edge TTS."
    )
    parser.add_argument(
        "--text",
        required=True,
        help="The narration text to speak.",
    )
    parser.add_argument(
        "--voice",
        default="en-US-AndrewNeural",
        help="The voice to use (default: en-US-GuyNeural).",
    )
    parser.add_argument(
        "--output",
        default="output/voice_test.mp3",
        help="Output MP3 file path.",
    )

    args = parser.parse_args()

    try:
        asyncio.run(
            generate_voice(
                text=args.text,
                voice=args.voice,
                output=Path(args.output),
            )
        )
    except Exception as error:
        raise SystemExit(f"Narration generation failed: {error}")


if __name__ == "__main__":
    main()
