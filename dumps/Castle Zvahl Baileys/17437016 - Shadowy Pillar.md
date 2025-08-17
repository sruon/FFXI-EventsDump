# 17437016 - Shadowy Pillar

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Castle Zvahl Baileys (ID: 161) |
| Block Size       | 516 bytes                      |
| Total Events     | 2                              |
| References Count | 25                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [100](#event-100)     | 0x0001       |    391 |             92 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x1DA5      |        7589 |
|       3 | 0x1DA6      |        7590 |
|       4 | 0x1DA7      |        7591 |
|       5 | 0x1DA9      |        7593 |
|       6 | 0x1DAA      |        7594 |
|       7 | 0x1DAB      |        7595 |
|       8 | 0x0008      |           8 |
|       9 | 0x1DAC      |        7596 |
|      10 | 0x0484      |        1156 |
|      11 | 0x1DAD      |        7597 |
|      12 | 0x1DAE      |        7598 |
|      13 | 0x1DAF      |        7599 |
|      14 | 0x1DB0      |        7600 |
|      15 | 0x1DA8      |        7592 |
|      16 | 0x0002      |           2 |
|      17 | 0x1DB1      |        7601 |
|      18 | 0x0003      |           3 |
|      19 | 0x0483      |        1155 |
|      20 | 0x1DB7      |        7607 |
|      21 | 0x1DB8      |        7608 |
|      22 | 0x1DB9      |        7609 |
|      23 | 0x0004      |           4 |
|      24 | 0x1DB6      |        7606 |

## String References

- **7591**: Are you ready, kupo? [You bet I am!/Maybe later.]
- **7594**: Listen to the rules? [Yes./No.]
- **7599**: Get it, kupo? [Got it./Not exactly...]

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

### Event 100

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 391 bytes |
| Instructions | 58        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 03 01 10 00  80 03 00 00 02 10 03 02    .B............
0010: 10 00 80 29 80 57 11 0A  01 03 02 00 00 01 80 80  ...).W..........
0020: 1B 01 2B 57 11 0A 01 02  80 23 2B 57 11 0A 01 03  ..+W.....#+W....
0030: 80 23 24 04 80 01 80 00  80 25 02 00 10 00 80 00  .#$......%......
0040: 04 01 2B 57 11 0A 01 05  80 23 24 06 80 00 80 00  ..+W.....#$.....
0050: 80 25 02 00 10 00 80 00  E8 00 2B 57 11 0A 01 07  .%........+W....
0060: 80 23 03 02 10 08 80 2B  57 11 0A 01 09 80 23 03  .#.....+W.....#.
0070: 02 10 0A 80 2B 57 11 0A  01 0B 80 23 2B 57 11 0A  ....+W.....#+W..
0080: 01 0C 80 23 02 01 00 00  80 00 E5 00 24 0D 80 01  ...#........$...
0090: 80 00 80 25 02 00 10 00  80 00 AD 00 2B 57 11 0A  ...%........+W..
00A0: 01 0E 80 23 03 01 10 01  80 21 01 E2 00 02 00 10  ...#.....!......
00B0: 01 80 00 E2 00 2B 57 11  0A 01 07 80 23 03 02 10  .....+W.....#...
00C0: 08 80 2B 57 11 0A 01 09  80 23 03 02 10 0A 80 2B  ..+W.....#.....+
00D0: 57 11 0A 01 0B 80 23 2B  57 11 0A 01 0C 80 23 01  W.....#+W.....#.
00E0: E2 00 01 84 00 01 01 01  02 00 10 01 80 00 01 01  ................
00F0: 2B 57 11 0A 01 0E 80 23  03 01 10 01 80 21 01 01  +W.....#.....!..
0100: 01 01 18 01 02 00 10 01  80 00 18 01 2B 57 11 0A  ............+W..
0110: 01 0F 80 23 21 01 18 01  01 7E 01 02 00 00 10 80  ...#!....~......
0120: 80 34 01 2B 57 11 0A 01  11 80 23 03 01 10 10 80  .4.+W.....#.....
0130: 21 01 7E 01 02 00 00 12  80 80 6A 01 2B 57 11 0A  !.~.......j.+W..
0140: 01 02 80 23 03 02 10 13  80 2B 57 11 0A 01 14 80  ...#.....+W.....
0150: 23 03 02 10 13 80 2B 57  11 0A 01 15 80 23 2B 57  #.....+W.....#+W
0160: 11 0A 01 16 80 23 21 01  7E 01 02 00 00 17 80 80  .....#!.~.......
0170: 7E 01 2B 57 11 0A 01 18  80 23 21 01 7E 01 29 80  ~.+W.....#!.~.).
0180: 57 11 0A 01 04 20 00 00                           W.... ..        
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x03] Work_Zone[1] = 0*
  3: 0x0009 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  4: 0x000E [0x03] Work_Zone[2] = 0*
  5: 0x0013 [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Stooge Moogle (ID: 17437015/0x010A1157), tag_num=0x03)
  6: 0x001A [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x011B
  7: 0x0022 [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7589*]:
    → "Well, folks, [he's/she's] tamed the elements and matched wits with the great wyrm! Now, all that stands between our brave contestant and victory is... <Dum-dum-dum>...The Gauuuntlet of Fooortitude!"
  8: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002A [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7590*]:
    → "So what say you, friend? Only those with nerves of darksteel should dare challenge... <Dum-dum-dum>...The Gauuuntlet of Fooortitude!"
 10: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0032 [0x24] CREATE_DIALOG(message_id=7591*, default_option=1*, option_flags=0*)
    → "Are you ready, kupo? [You bet I am!/Maybe later.]"
 12: 0x0039 [0x25] WAIT_DIALOG_SELECT()
 13: 0x003A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0104
 14: 0x0042 [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7593*]:
    → "Splendid! Ladies and gentlemen, our brave challenger will enter the fray! Do you need to hear the rules before you begin, kupo?"
 15: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x004A [0x24] CREATE_DIALOG(message_id=7594*, default_option=0*, option_flags=0*)
    → "Listen to the rules? [Yes./No.]"
 17: 0x0051 [0x25] WAIT_DIALOG_SELECT()
 18: 0x0052 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00E8
 19: 0x005A [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7595*]:
    → "Welcome to... <Dum-dum-dum>...The Gauuuntlet of Fooortitude! The rules of this challenge are simple indeed."
 20: 0x0061 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0062 [0x03] Work_Zone[2] = 8*
 22: 0x0067 [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7596*]:
    → "Make your way to the Flame of Fate within the allotted span of $0 minutes (Earth time) and victory is yours, kupo!"
 23: 0x006E [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x006F [0x03] Work_Zone[2] = 1156*
 25: 0x0074 [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7597*]:
    → "Victorious contestants will receive $6 as recompense for their valor in the face of adversity!"
 26: 0x007B [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x007C [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7598*]:
    → "There is one catch, kupo. You must face the test as the fledgling adventurer you once were--with nothing but the courage of your convictions! (Your level will be reduced to one for the duration of the challenge.)"
 28: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x0084 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x00E5
 30: 0x008C [0x24] CREATE_DIALOG(message_id=7599*, default_option=1*, option_flags=0*)
    → "Get it, kupo? [Got it./Not exactly...]"
 31: 0x0093 [0x25] WAIT_DIALOG_SELECT()
 32: 0x0094 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00AD
 33: 0x009C [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7600*]:
    → "Excellent! May the Goddess be with you on your journey through... <Dum-dum-dum>...The Gauuuntlet of Fooortitude!"
 34: 0x00A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x00A4 [0x03] Work_Zone[1] = 1*
 36: 0x00A9 [0x21] END_EVENT

SUBROUTINE_00E2:
 37: 0x00E2 [0x01] GOTO 0x0084
 38: 0x00E5 [0x01] GOTO 0x0101
 39: 0x00E8 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0101
 40: 0x00F0 [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7600*]:
    → "Excellent! May the Goddess be with you on your journey through... <Dum-dum-dum>...The Gauuuntlet of Fooortitude!"
 41: 0x00F7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x00F8 [0x03] Work_Zone[1] = 1*
 43: 0x00FD [0x21] END_EVENT

SUBROUTINE_0101:
 44: 0x0101 [0x01] GOTO 0x0118
 45: 0x0104 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0118
 46: 0x010C [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7592*]:
    → "Oh, of course! You just need more time to think about it, right? It's not that you're...<cough>...chicken, or anything like that."
 47: 0x0113 [0x23] WAIT_FOR_DIALOG_INTERACTION
 48: 0x0114 [0x21] END_EVENT

SUBROUTINE_0118:
 49: 0x0118 [0x01] GOTO 0x017E
 50: 0x011B [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x0134
 51: 0x0123 [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7601*]:
    → "What are you still doing here!? The goal's that-a-way, you know! Now chop chop, kupo!"
 52: 0x012A [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x012B [0x03] Work_Zone[1] = 2*
 54: 0x0130 [0x21] END_EVENT

SUBROUTINE_017E:
 55: 0x017E [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Stooge Moogle (ID: 17437015/0x010A1157), tag_num=0x04)
 56: 0x0185 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 57: 0x0187 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00AA [0x01] GOTO 0x00E2
# Dead code (unreachable instructions):
     0x00FE [0x01] GOTO 0x0101
# Dead code (unreachable instructions):
     0x0115 [0x01] GOTO 0x0118
# Dead code (unreachable instructions):
     0x0131 [0x01] GOTO 0x017E
     0x0167 [0x01] GOTO 0x017E
     0x017B [0x01] GOTO 0x017E
```
