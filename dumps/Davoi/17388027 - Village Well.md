# 17388027 - Village Well

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Davoi (ID: 149) |
| Block Size       | 316 bytes       |
| Total Events     | 3               |
| References Count | 15              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [113](#event-113)     | 0x0001       |    175 |             24 |
| [112](#event-112)     | 0x00B0       |     52 |             21 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x0013      |          19 |
|       3 | 0x1D31      |        7473 |
|       4 | 0x00DC      |         220 |
|       5 | 0x1D32      |        7474 |
|       6 | 0x003C      |          60 |
|       7 | 0x1D39      |        7481 |
|       8 | 0x0001      |           1 |
|       9 | 0x1D33      |        7475 |
|      10 | 0x1D34      |        7476 |
|      11 | 0x1D35      |        7477 |
|      12 | 0x1D36      |        7478 |
|      13 | 0x1D37      |        7479 |
|      14 | 0x1D38      |        7480 |

## String References

- **7473**: You work the pulley.
- **7474**: Dipping the letter into the water, you see words appear.
- **7475**: "Captain Exoroche: I, Chusarlaud, am no longer worthy to be a Royal Knight, for I have sold our secrets to the Orcs.
- **7476**: I spent my reward on medicine for my mother, but it was all in vain. Her death taught me the error of my ways, and I tried repeatedly to redeem myself.
- **7477**: But my partner Vilbert threatened to expose my treachery if I did not continue! Alas, he had me in the palm of his hand!
- **7478**: I had to take action! I decided to send this letter upon the close of today's training. I expect no forgiveness, but I must put a stop to this madness.
- **7479**: I have caused pain to my mother, and I have betrayed my kind captain. There is no other way!"
- **7480**: The letter ends abruptly.
- **7481**: Read the letter again? [Yes./No.]

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 113

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 175 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F   BE..........fdo
0010: 31 01 80 55 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  1..U..........fd
0020: 6F 31 38 02 80 48 03 80  23 45 00 80 F0 FF FF 7F  o18..H..#E......
0030: F0 FF FF 7F 66 64 69 31  01 80 55 00 80 F0 FF FF  ....fdi1..U.....
0040: 7F F0 FF FF 7F 66 64 69  31 03 02 10 04 80 48 05  .....fdi1.....H.
0050: 80 23 1C 06 80 1A C8 00  24 07 80 08 80 01 80 25  .#......$......%
0060: 02 00 10 01 80 00 6E 00  01 55 00 01 6E 00 45 00  ......n..U..n.E.
0070: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 01 80 55  .........fdo1..U
0080: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 45 00  ..........fdo1E.
0090: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 01 80 55  .........fdi1..U
00A0: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 21 00  ..........fdi1!.
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  2: 0x0013 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  3: 0x0022 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  4: 0x0025 [0x48] [System] [7473*]:
    → "You work the pulley."
  5: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0029 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x003A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
  8: 0x0049 [0x03] Work_Zone[2] = 220*
  9: 0x004E [0x48] [System] [7474*]:
    → "Dipping the letter into the water, you see words appear."
 10: 0x0051 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0052 [0x1C] WAIT(60* ticks)
 12: 0x0055 [0x1A] CALL_SUBROUTINE(address=0x00C8)
 13: 0x0058 [0x24] CREATE_DIALOG(message_id=7481*, default_option=1*, option_flags=0*)
    → "Read the letter again? [Yes./No.]"
 14: 0x005F [0x25] WAIT_DIALOG_SELECT()
 15: 0x0060 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x006E
 16: 0x0068 [0x01] GOTO 0x0055

SUBROUTINE_006E:
 17: 0x006E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x007F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 19: 0x008E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x009F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 21: 0x00AE [0x21] END_EVENT
 22: 0x00AF [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x006B [0x01] GOTO 0x006E
```

### Event 112

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 52 bytes |
| Instructions | 21       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 24 07 80 08 80 01 80 25  02 00 10 01 80 00 C6 00  $......%........
00C0: 1A C8 00 01 C6 00 21 00  48 09 80 23 48 0A 80 23  ......!.H..#H..#
00D0: 48 0B 80 23 48 0C 80 23  48 0D 80 23 1C 06 80 48  H..#H..#H..#...H
00E0: 0E 80 23 1B                                       ..#.            
```

#### Opcodes

```
  0: 0x00B0 [0x24] CREATE_DIALOG(message_id=7481*, default_option=1*, option_flags=0*)
    → "Read the letter again? [Yes./No.]"
  1: 0x00B7 [0x25] WAIT_DIALOG_SELECT()
  2: 0x00B8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00C6
  3: 0x00C0 [0x1A] CALL_SUBROUTINE(address=0x00C8)
  4: 0x00C3 [0x01] GOTO 0x00C6

SUBROUTINE_00C6:
  5: 0x00C6 [0x21] END_EVENT
  6: 0x00C7 [0x00] END_REQSTACK()

SUBROUTINE_00C8:
  7: 0x00C8 [0x48] [System] [7475*]:
    → ""Captain Exoroche: I, Chusarlaud, am no longer worthy to be a Royal Knight, for I have sold our secrets to the Orcs."
  8: 0x00CB [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00CC [0x48] [System] [7476*]:
    → "I spent my reward on medicine for my mother, but it was all in vain. Her death taught me the error of my ways, and I tried repeatedly to redeem myself."
 10: 0x00CF [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00D0 [0x48] [System] [7477*]:
    → "But my partner Vilbert threatened to expose my treachery if I did not continue! Alas, he had me in the palm of his hand!"
 12: 0x00D3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00D4 [0x48] [System] [7478*]:
    → "I had to take action! I decided to send this letter upon the close of today's training. I expect no forgiveness, but I must put a stop to this madness."
 14: 0x00D7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x00D8 [0x48] [System] [7479*]:
    → "I have caused pain to my mother, and I have betrayed my kind captain. There is no other way!""
 16: 0x00DB [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x00DC [0x1C] WAIT(60* ticks)
 18: 0x00DF [0x48] [System] [7480*]:
    → "The letter ends abruptly."
 19: 0x00E2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x00E3 [0x1B] RETURN
```
