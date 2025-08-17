# 16883831 - Eonnites Revelations

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 232 bytes                   |
| Total Events     | 2                           |
| References Count | 13                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [390](#event-390)     | 0x0001       |    153 |             47 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2B70      |       11120 |
|       1 | 0x0000      |           0 |
|       2 | 0x2B71      |       11121 |
|       3 | 0x0001      |           1 |
|       4 | 0x2B89      |       11145 |
|       5 | 0x2B72      |       11122 |
|       6 | 0x2B73      |       11123 |
|       7 | 0x2B74      |       11124 |
|       8 | 0x2B75      |       11125 |
|       9 | 0x2B76      |       11126 |
|      10 | 0x2B77      |       11127 |
|      11 | 0x2B78      |       11128 |
|      12 | 0x2B79      |       11129 |

## String References

- **11120**: Read the scripture? [Yes./No.]
- **11121**: Long, long ago, an ancient race, descended from the gods, flourished in Vana'diel.
- **11122**: They traveled through the sky, extracted gold from stones, and gave birth to grasslands across the world.
- **11123**: But one day, they decided to build a pathway to the divine entrance of Paradise.
- **11124**: Enraged by such a brazen display of insolence, the gatekeeper destroyed their path and cast their homes to the bottom of the sea.
- **11125**: Shortly thereafter, the goddess Altana awakened and saw the ruin that had once been Vana'diel. Saddened, She wept five divine tears.
- **11126**: When the five tears fell upon the earth, they gave life to the five races of Vana'diel.
- **11127**: But the god Promathia saw this from His place in the shadows. The Twilight God saw fit to condemn Altana's work, cursing the people with eternal conflict amongst themselves.
- **11128**: He created terrible beasts and spread them across the world, commanding them to fight the people of Vana'diel and occupy their minds.
- **11129**: Never again would they think to open the Gate of the Gods.
- **11145**: 

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

### Event 390

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 153 bytes |
| Instructions | 47        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    9C 00 00 4A F0 FF FF  7F F8 FF FF 7F 24 00 80   ...J........$..
0010: 01 80 01 80 25 02 00 10  01 80 00 98 00 48 02 80  ....%........H..
0020: 23 02 00 00 03 80 00 2D  00 48 04 80 23 48 05 80  #......-.H..#H..
0030: 23 48 06 80 23 02 00 00  03 80 00 41 00 48 04 80  #H..#......A.H..
0040: 23 48 07 80 23 02 00 00  03 80 00 51 00 48 04 80  #H..#......Q.H..
0050: 23 48 08 80 23 02 00 00  03 80 00 61 00 48 04 80  #H..#......a.H..
0060: 23 48 09 80 23 02 00 00  03 80 00 71 00 48 04 80  #H..#......q.H..
0070: 23 48 0A 80 23 02 00 00  03 80 00 81 00 48 04 80  #H..#........H..
0080: 23 48 0B 80 23 02 00 00  03 80 00 91 00 48 04 80  #H..#........H..
0090: 23 48 0C 80 23 01 98 00  21 00                    #H..#...!.      
```

#### Opcodes

```
  0: 0x0001 [0x9C] STORE_CLIENT_LANGUAGE_ID(result=0x00)
  1: 0x0004 [0x4A] LocalPlayer looks at EventEntity
  2: 0x000D [0x24] CREATE_DIALOG(message_id=11120*, default_option=0*, option_flags=0*)
    → "Read the scripture? [Yes./No.]"
  3: 0x0014 [0x25] WAIT_DIALOG_SELECT()
  4: 0x0015 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0098
  5: 0x001D [0x48] [System] [11121*]:
    → "Long, long ago, an ancient race, descended from the gods, flourished in Vana'diel."
  6: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0021 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x002D
  8: 0x0029 [0x48] [System] [11145*]:
    → ""
  9: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002D [0x48] [System] [11122*]:
    → "They traveled through the sky, extracted gold from stones, and gave birth to grasslands across the world."
 11: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0031 [0x48] [System] [11123*]:
    → "But one day, they decided to build a pathway to the divine entrance of Paradise."
 13: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0035 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0041
 15: 0x003D [0x48] [System] [11145*]:
    → ""
 16: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0041 [0x48] [System] [11124*]:
    → "Enraged by such a brazen display of insolence, the gatekeeper destroyed their path and cast their homes to the bottom of the sea."
 18: 0x0044 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0045 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0051
 20: 0x004D [0x48] [System] [11145*]:
    → ""
 21: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0051 [0x48] [System] [11125*]:
    → "Shortly thereafter, the goddess Altana awakened and saw the ruin that had once been Vana'diel. Saddened, She wept five divine tears."
 23: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0055 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0061
 25: 0x005D [0x48] [System] [11145*]:
    → ""
 26: 0x0060 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0061 [0x48] [System] [11126*]:
    → "When the five tears fell upon the earth, they gave life to the five races of Vana'diel."
 28: 0x0064 [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x0065 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0071
 30: 0x006D [0x48] [System] [11145*]:
    → ""
 31: 0x0070 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0071 [0x48] [System] [11127*]:
    → "But the god Promathia saw this from His place in the shadows. The Twilight God saw fit to condemn Altana's work, cursing the people with eternal conflict amongst themselves."
 33: 0x0074 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x0075 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0081
 35: 0x007D [0x48] [System] [11145*]:
    → ""
 36: 0x0080 [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x0081 [0x48] [System] [11128*]:
    → "He created terrible beasts and spread them across the world, commanding them to fight the people of Vana'diel and occupy their minds."
 38: 0x0084 [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x0085 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0091
 40: 0x008D [0x48] [System] [11145*]:
    → ""
 41: 0x0090 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x0091 [0x48] [System] [11129*]:
    → "Never again would they think to open the Gate of the Gods."
 43: 0x0094 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x0095 [0x01] GOTO 0x0098

SUBROUTINE_0098:
 45: 0x0098 [0x21] END_EVENT
 46: 0x0099 [0x00] END_REQSTACK()
```
