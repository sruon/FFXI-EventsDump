# 17490311 - GoalPoint

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Kuftal Tunnel (ID: 174) |
| Block Size       | 312 bytes               |
| Total Events     | 3                       |
| References Count | 16                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [22](#event-22)       | 0x0001       |     81 |             17 |
| [23](#event-23)       | 0x0052       |    138 |             28 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0040      |          64 |
|       2 | 0x0014      |          20 |
|       3 | 0x1CFB      |        7419 |
|       4 | 0x1CFC      |        7420 |
|       5 | 0x1CFD      |        7421 |
|       6 | 0x1CFE      |        7422 |
|       7 | 0x1CFF      |        7423 |
|       8 | 0x0003      |           3 |
|       9 | 0x1D00      |        7424 |
|      10 | 0x0001      |           1 |
|      11 | 0x1D01      |        7425 |
|      12 | 0x0002      |           2 |
|      13 | 0x1D02      |        7426 |
|      14 | 0x1D03      |        7427 |
|      15 | 0x1D04      |        7428 |

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

### Event 22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 81 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    6C 8D E1 0A 01 00 80  00 80 4E 00 8D E1 0A 01   l........N.....
0010: 6C 8D E1 0A 01 01 80 02  80 2B 8D E1 0A 01 03 80  l........+......
0020: 23 2B 8D E1 0A 01 04 80  23 2B 8D E1 0A 01 05 80  #+......#+......
0030: 23 2B 8D E1 0A 01 06 80  23 2B 8D E1 0A 01 07 80  #+......#+......
0040: 23 6C 8D E1 0A 01 00 80  02 80 4E 01 8D E1 0A 01  #l........N.....
0050: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x6C] FADE_ENTITY_COLOR(entity_id=Moogle (ID: 17490317/0x010AE18D), end_alpha=0*, fade_time=0*)
  1: 0x000A [0x4E] SET_ENTITY_HIDE_FLAG: Show Moogle (ID: 17490317/0x010AE18D)
  2: 0x0010 [0x6C] FADE_ENTITY_COLOR(entity_id=Moogle (ID: 17490317/0x010AE18D), end_alpha=64*, fade_time=20*)
  3: 0x0019 [0x2B] Moogle (ID: 17490317/0x010AE18D) [7419*]:
    → "Boo-hah-hah`...kupo!"
  4: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0021 [0x2B] Moogle (ID: 17490317/0x010AE18D) [7420*]:
    → "Huh? Why aren't you jumping out of your skin in absolute terror? I would've died of fright, kupo!"
  6: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0029 [0x2B] Moogle (ID: 17490317/0x010AE18D) [7421*]:
    → "Here, take this as a testament to your courage. Exchange it for the item your partner received so you can prove that you both reached the goal safely, kupo!"
  8: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0031 [0x2B] Moogle (ID: 17490317/0x010AE18D) [7422*]:
    → "Return with the evidence of your success to the moogle in town. Handing over your partner's item will prove that you were both able to reach me, kupo!"
 10: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0039 [0x2B] Moogle (ID: 17490317/0x010AE18D) [7423*]:
    → "Oh, and here's a picture of how your partner's face looked when I popped out of nowhere to scare you. You should hand this in at the same time, kupo! Kupupupu..."
 12: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0041 [0x6C] FADE_ENTITY_COLOR(entity_id=Moogle (ID: 17490317/0x010AE18D), end_alpha=0*, fade_time=20*)
 14: 0x004A [0x4E] SET_ENTITY_HIDE_FLAG: Hide Moogle (ID: 17490317/0x010AE18D)
 15: 0x0050 [0x21] END_EVENT
 16: 0x0051 [0x00] END_REQSTACK()
```

### Event 23

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0052    |
| Data Size    | 138 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       6C 8D E1 0A 01 00  80 00 80 4E 00 8D E1 0A    l........N....
0060: 01 6C 8D E1 0A 01 01 80  02 80 13 00 00 08 80 02  .l..............
0070: 00 00 00 80 80 82 00 2B  8D E1 0A 01 09 80 23 01  .......+......#.
0080: CB 00 02 00 00 0A 80 80  9D 00 2B 8D E1 0A 01 03  ..........+.....
0090: 80 23 2B 8D E1 0A 01 0B  80 23 01 CB 00 02 00 00  .#+......#......
00A0: 0C 80 80 B8 00 2B 8D E1  0A 01 0D 80 23 2B 8D E1  .....+......#+..
00B0: 0A 01 0E 80 23 01 CB 00  02 00 00 08 80 80 CB 00  ....#...........
00C0: 2B 8D E1 0A 01 0F 80 23  01 CB 00 6C 8D E1 0A 01  +......#...l....
00D0: 00 80 02 80 4E 01 8D E1  0A 01 21 00              ....N.....!.    
```

#### Opcodes

```
  0: 0x0052 [0x6C] FADE_ENTITY_COLOR(entity_id=Moogle (ID: 17490317/0x010AE18D), end_alpha=0*, fade_time=0*)
  1: 0x005B [0x4E] SET_ENTITY_HIDE_FLAG: Show Moogle (ID: 17490317/0x010AE18D)
  2: 0x0061 [0x6C] FADE_ENTITY_COLOR(entity_id=Moogle (ID: 17490317/0x010AE18D), end_alpha=64*, fade_time=20*)
  3: 0x006A [0x13] ExtData[1]->WorkLocal[0] = rand() % 3*
  4: 0x006F [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0082
  5: 0x0077 [0x2B] Moogle (ID: 17490317/0x010AE18D) [7424*]:
    → "This place is crawling with nasties. You should probably head back to town so you can testify to your partner's bravery."
  6: 0x007E [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x007F [0x01] GOTO 0x00CB
  8: 0x0082 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x009D
  9: 0x008A [0x2B] Moogle (ID: 17490317/0x010AE18D) [7419*]:
    → "Boo-hah-hah`...kupo!"
 10: 0x0091 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0092 [0x2B] Moogle (ID: 17490317/0x010AE18D) [7425*]:
    → "Why do ghosts say "boo," anyway?"
 12: 0x0099 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x009A [0x01] GOTO 0x00CB
 14: 0x009D [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x00B8
 15: 0x00A5 [0x2B] Moogle (ID: 17490317/0x010AE18D) [7426*]:
    → "I heard that going to a dark, scary dungeon is the best way to test your courage. This place definitely qualifies, kupo!"
 16: 0x00AC [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x00AD [0x2B] Moogle (ID: 17490317/0x010AE18D) [7427*]:
    → "Maybe I'm doing something wrong, kupo?"
 18: 0x00B4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x00B5 [0x01] GOTO 0x00CB
 20: 0x00B8 [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x00CB
 21: 0x00C0 [0x2B] Moogle (ID: 17490317/0x010AE18D) [7428*]:
    → "If it gets out that I haven't scared the wits out of a single person yet, I'm going to get into trouble, kupo..."
 22: 0x00C7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x00C8 [0x01] GOTO 0x00CB

SUBROUTINE_00CB:
 24: 0x00CB [0x6C] FADE_ENTITY_COLOR(entity_id=Moogle (ID: 17490317/0x010AE18D), end_alpha=0*, fade_time=20*)
 25: 0x00D4 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Moogle (ID: 17490317/0x010AE18D)
 26: 0x00DA [0x21] END_EVENT
 27: 0x00DB [0x00] END_REQSTACK()
```
