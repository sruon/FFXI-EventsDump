# 17863456 - Ergon Locus

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Morimar Basalt Fields (ID: 265) |
| Block Size       | 428 bytes                       |
| Total Events     | 2                               |
| References Count | 16                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [3007](#event-3007)   | 0x0001       |    338 |             78 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0009      |           9 |
|       2 | 0x0001      |           1 |
|       3 | 0x000A      |          10 |
|       4 | 0x0002      |           2 |
|       5 | 0x000B      |          11 |
|       6 | 0x0003      |           3 |
|       7 | 0x0010      |          16 |
|       8 | 0x1D87      |        7559 |
|       9 | 0x1D88      |        7560 |
|      10 | 0x40000000  |  1073741824 |
|      11 | 0x1D89      |        7561 |
|      12 | 0x002D      |          45 |
|      13 | 0x0078      |         120 |
|      14 | 0x1D8A      |        7562 |
|      15 | 0x1D8B      |        7563 |

## String References

- **7559**: This seems to be the site of the ergon locus oft called the "[/Flourishing Island/Bud of the Swarm/Luminous Isle/Immutable Boulder/Immaculate Sands/Fruit of Fecundity/Dragon Driftwood/Torchbloom/Spring of Prosperity/Snowdrift Arbor/Frostbloom/Prominence of the Gales/Lake of Light/Sweltering Spring/Prominence of the Flame]." It is most likely worth surveying.
- **7560**: This seems to be the site of the ergon locus oft called the "[Sanctum of Life/Prominence of the Soil/Pool of Clarity/Bryophitic Boulder/Overgrown Grove/Whitewater Arbor/Bud of the Fragrant Breeze/Crag of the Triumvirate/Prominence of the Ripple/Saliferous Spring/Loch of Flux/Lambent Pillar/Crystalline Claw/Prominence of the Rime/Halcyon Icefall]." It is most likely worth surveying.
- **7561**: Commence survey? [Yes./No.]
- **7562**: [Your survey is a success./You have already surveyed an ergon locus in the area.] Return to the manager in charge and report on what you have learned about the ergon locus's attributes.
- **7563**: Your survey has ended in utter failure. The time of day and distance from which you surveyed could very well be to blame.

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

### Event 3007

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 338 bytes |
| Instructions | 78        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 02 00 00 80 03 00  00 02 10 03 01 00 03 10   ...............
0010: 1E F0 FF FF 7F 6F 70 02  00 00 00 80 80 7F 00 02  .....op.........
0020: 02 00 00 80 80 2F 00 03  02 10 01 80 01 5F 00 02  ...../......._..
0030: 02 00 02 80 80 3F 00 03  02 10 03 80 01 5F 00 02  .....?......._..
0040: 02 00 04 80 80 4F 00 03  02 10 05 80 01 5F 00 02  .....O......._..
0050: 02 00 06 80 80 5F 00 03  02 10 00 80 01 5F 00 02  ....._......._..
0060: 02 10 07 80 03 6E 00 48  08 80 23 01 77 00 08 02  .....n.H..#.w...
0070: 10 07 80 48 09 80 23 03  01 10 0A 80 01 50 01 02  ...H..#......P..
0080: 00 00 02 80 80 37 01 02  02 00 00 80 80 97 00 03  .....7..........
0090: 02 10 01 80 01 C7 00 02  02 00 02 80 80 A7 00 03  ................
00A0: 02 10 03 80 01 C7 00 02  02 00 04 80 80 B7 00 03  ................
00B0: 02 10 05 80 01 C7 00 02  02 00 06 80 80 C7 00 03  ................
00C0: 02 10 00 80 01 C7 00 02  02 10 07 80 03 D6 00 48  ...............H
00D0: 08 80 23 01 DF 00 08 02  10 07 80 48 09 80 23 24  ..#........H..#$
00E0: 0B 80 02 80 00 80 25 02  00 10 00 80 00 24 01 6E  ......%......$.n
00F0: F0 FF FF 7F 0C 80 99 F0  FF FF 7F 1C 0D 80 02 01  ................
0100: 00 02 80 00 18 01 42 03  02 10 00 80 48 0E 80 23  ......B.....H..#
0110: 03 01 10 02 80 01 21 01  48 0F 80 23 03 01 10 01  ......!.H..#....
0120: 10 01 34 01 02 00 10 02  80 00 34 01 03 01 10 0A  ..4.......4.....
0130: 80 01 34 01 01 50 01 02  00 00 04 80 80 50 01 03  ..4..P.......P..
0140: 02 10 02 80 48 0E 80 23  03 01 10 0A 80 01 50 01  ....H..#......P.
0150: 42 21 00                                          B!.             
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[2] = 0*
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  2: 0x000B [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  3: 0x0010 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0016 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0017 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x007F
  7: 0x001F [0x02] IF !(ExtData[1]->WorkLocal[2] == 0*) GOTO 0x002F
  8: 0x0027 [0x03] Work_Zone[2] = 9*
  9: 0x002C [0x01] GOTO 0x005F
 10: 0x002F [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x003F
 11: 0x0037 [0x03] Work_Zone[2] = 10*
 12: 0x003C [0x01] GOTO 0x005F
 13: 0x003F [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x004F
 14: 0x0047 [0x03] Work_Zone[2] = 11*
 15: 0x004C [0x01] GOTO 0x005F
 16: 0x004F [0x02] IF !(ExtData[1]->WorkLocal[2] == 3*) GOTO 0x005F
 17: 0x0057 [0x03] Work_Zone[2] = 0*
 18: 0x005C [0x01] GOTO 0x005F

SUBROUTINE_005F:
 19: 0x005F [0x02] IF !(Work_Zone[2] >= 16*) GOTO 0x006E
 20: 0x0067 [0x48] [System] [7559*]:
    → "This seems to be the site of the ergon locus oft called the "[/Flourishing Island/Bud of the Swarm/Luminous Isle/Immutable Boulder/Immaculate Sands/Fruit of Fecundity/Dragon Driftwood/Torchbloom/Spring of Prosperity/Snowdrift Arbor/Frostbloom/Prominence of the Gales/Lake of Light/Sweltering Spring/Prominence of the Flame]." It is most likely worth surveying."
 21: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x006B [0x01] GOTO 0x0077
 23: 0x006E [0x08] Work_Zone[2] -= 16*
 24: 0x0073 [0x48] [System] [7560*]:
    → "This seems to be the site of the ergon locus oft called the "[Sanctum of Life/Prominence of the Soil/Pool of Clarity/Bryophitic Boulder/Overgrown Grove/Whitewater Arbor/Bud of the Fragrant Breeze/Crag of the Triumvirate/Prominence of the Ripple/Saliferous Spring/Loch of Flux/Lambent Pillar/Crystalline Claw/Prominence of the Rime/Halcyon Icefall]." It is most likely worth surveying."
 25: 0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0077:
 26: 0x0077 [0x03] Work_Zone[1] = 1073741824*
 27: 0x007C [0x01] GOTO 0x0150
 28: 0x007F [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0137
 29: 0x0087 [0x02] IF !(ExtData[1]->WorkLocal[2] == 0*) GOTO 0x0097
 30: 0x008F [0x03] Work_Zone[2] = 9*
 31: 0x0094 [0x01] GOTO 0x00C7
 32: 0x0097 [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x00A7
 33: 0x009F [0x03] Work_Zone[2] = 10*
 34: 0x00A4 [0x01] GOTO 0x00C7
 35: 0x00A7 [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x00B7
 36: 0x00AF [0x03] Work_Zone[2] = 11*
 37: 0x00B4 [0x01] GOTO 0x00C7
 38: 0x00B7 [0x02] IF !(ExtData[1]->WorkLocal[2] == 3*) GOTO 0x00C7
 39: 0x00BF [0x03] Work_Zone[2] = 0*
 40: 0x00C4 [0x01] GOTO 0x00C7

SUBROUTINE_00C7:
 41: 0x00C7 [0x02] IF !(Work_Zone[2] >= 16*) GOTO 0x00D6
 42: 0x00CF [0x48] [System] [7559*]:
    → "This seems to be the site of the ergon locus oft called the "[/Flourishing Island/Bud of the Swarm/Luminous Isle/Immutable Boulder/Immaculate Sands/Fruit of Fecundity/Dragon Driftwood/Torchbloom/Spring of Prosperity/Snowdrift Arbor/Frostbloom/Prominence of the Gales/Lake of Light/Sweltering Spring/Prominence of the Flame]." It is most likely worth surveying."
 43: 0x00D2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x00D3 [0x01] GOTO 0x00DF
 45: 0x00D6 [0x08] Work_Zone[2] -= 16*
 46: 0x00DB [0x48] [System] [7560*]:
    → "This seems to be the site of the ergon locus oft called the "[Sanctum of Life/Prominence of the Soil/Pool of Clarity/Bryophitic Boulder/Overgrown Grove/Whitewater Arbor/Bud of the Fragrant Breeze/Crag of the Triumvirate/Prominence of the Ripple/Saliferous Spring/Loch of Flux/Lambent Pillar/Crystalline Claw/Prominence of the Rime/Halcyon Icefall]." It is most likely worth surveying."
 47: 0x00DE [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00DF:
 48: 0x00DF [0x24] CREATE_DIALOG(message_id=7561*, default_option=1*, option_flags=0*)
    → "Commence survey? [Yes./No.]"
 49: 0x00E6 [0x25] WAIT_DIALOG_SELECT()
 50: 0x00E7 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0124
 51: 0x00EF [0x6E] LocalPlayer uses emote 45*
 52: 0x00F6 [0x99] Wait for LocalPlayer animation to complete
 53: 0x00FB [0x1C] WAIT(120* ticks)
 54: 0x00FE [0x02] IF !(ExtData[1]->WorkLocal[1] == 1*) GOTO 0x0118
 55: 0x0106 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 56: 0x0107 [0x03] Work_Zone[2] = 0*
 57: 0x010C [0x48] [System] [7562*]:
    → "[Your survey is a success./You have already surveyed an ergon locus in the area.] Return to the manager in charge and report on what you have learned about the ergon locus's attributes."
 58: 0x010F [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x0110 [0x03] Work_Zone[1] = 1*
 60: 0x0115 [0x01] GOTO 0x0121
 61: 0x0118 [0x48] [System] [7563*]:
    → "Your survey has ended in utter failure. The time of day and distance from which you surveyed could very well be to blame."
 62: 0x011B [0x23] WAIT_FOR_DIALOG_INTERACTION
 63: 0x011C [0x03] Work_Zone[1] = Work_Zone[1]

SUBROUTINE_0121:
 64: 0x0121 [0x01] GOTO 0x0134
 65: 0x0124 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0134
 66: 0x012C [0x03] Work_Zone[1] = 1073741824*
 67: 0x0131 [0x01] GOTO 0x0134

SUBROUTINE_0134:
 68: 0x0134 [0x01] GOTO 0x0150
 69: 0x0137 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x0150
 70: 0x013F [0x03] Work_Zone[2] = 1*
 71: 0x0144 [0x48] [System] [7562*]:
    → "[Your survey is a success./You have already surveyed an ergon locus in the area.] Return to the manager in charge and report on what you have learned about the ergon locus's attributes."
 72: 0x0147 [0x23] WAIT_FOR_DIALOG_INTERACTION
 73: 0x0148 [0x03] Work_Zone[1] = 1073741824*
 74: 0x014D [0x01] GOTO 0x0150

SUBROUTINE_0150:
 75: 0x0150 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 76: 0x0151 [0x21] END_EVENT
 77: 0x0152 [0x00] END_REQSTACK()
```
