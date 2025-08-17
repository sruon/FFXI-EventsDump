# 17437017 - Flame of Fate

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Castle Zvahl Baileys (ID: 161) |
| Block Size       | 224 bytes                      |
| Total Events     | 2                              |
| References Count | 11                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [101](#event-101)     | 0x0001       |    153 |             35 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0484      |        1156 |
|       3 | 0x1DB2      |        7602 |
|       4 | 0x0002      |           2 |
|       5 | 0x1DB4      |        7604 |
|       6 | 0x1DB5      |        7605 |
|       7 | 0x1DB6      |        7606 |
|       8 | 0x0003      |           3 |
|       9 | 0x0004      |           4 |
|      10 | 0x1DB3      |        7603 |

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

### Event 101

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 153 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 03 01 10 00  80 03 00 00 02 10 03 02    .B............
0010: 10 01 80 29 80 57 11 0A  01 03 02 00 00 01 80 80  ...).W..........
0020: 37 00 03 02 10 02 80 2B  57 11 0A 01 03 80 23 03  7......+W.....#.
0030: 01 10 04 80 01 8F 00 02  00 00 04 80 80 64 00 2B  .............d.+
0040: 57 11 0A 01 05 80 23 03  02 10 02 80 2B 57 11 0A  W.....#.....+W..
0050: 01 06 80 23 2B 57 11 0A  01 07 80 23 03 01 10 01  ...#+W.....#....
0060: 80 01 8F 00 02 00 00 08  80 80 77 00 2B 57 11 0A  ..........w.+W..
0070: 01 07 80 23 01 8F 00 02  00 00 09 80 80 8F 00 03  ...#............
0080: 02 10 02 80 2B 57 11 0A  01 0A 80 23 01 8F 00 21  ....+W.....#...!
0090: 29 80 57 11 0A 01 04 20  00 00                    ).W.... ..      
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x03] Work_Zone[1] = 0*
  3: 0x0009 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  4: 0x000E [0x03] Work_Zone[2] = 1*
  5: 0x0013 [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Stooge Moogle (ID: 17437015/0x010A1157), tag_num=0x03)
  6: 0x001A [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0037
  7: 0x0022 [0x03] Work_Zone[2] = 1156*
  8: 0x0027 [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7602*]:
    → "<Bzzzzzz!> Ohhhhhh, I'm sorry. That sound means you're out of time! Well, [he/she] gave it [his/her] best shot, folks. Come back whenever you're ready to take another shot at... <Dum-dum-dum>...The Gauuuntlet of Fooortitude!"
  9: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002F [0x03] Work_Zone[1] = 2*
 11: 0x0034 [0x01] GOTO 0x008F
 12: 0x0037 [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x0064
 13: 0x003F [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7604*]:
    → "[He's/She's] done it, folks! [He's/She's] conquered... <Dum-dum-dum>...The Gauuuntlet of Fooortitude!"
 14: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0047 [0x03] Work_Zone[2] = 1156*
 16: 0x004C [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7605*]:
    → "And here's your reward: $6, kupo!"
 17: 0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0054 [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7606*]:
    → "You'll be able to redeem this for a truly spectacular prize at our souvenir booth in the Castle Zvahl Keep, so what are you waiting for? Go claim your well-deserved loot, kupo!"
 19: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x005C [0x03] Work_Zone[1] = 1*
 21: 0x0061 [0x01] GOTO 0x008F
 22: 0x0064 [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x0077
 23: 0x006C [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7606*]:
    → "You'll be able to redeem this for a truly spectacular prize at our souvenir booth in the Castle Zvahl Keep, so what are you waiting for? Go claim your well-deserved loot, kupo!"
 24: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0074 [0x01] GOTO 0x008F
 26: 0x0077 [0x02] IF !(ExtData[1]->WorkLocal[0] == 4*) GOTO 0x008F
 27: 0x007F [0x03] Work_Zone[2] = 1156*
 28: 0x0084 [0x2B] Stooge Moogle (ID: 17437015/0x010A1157) [7603*]:
    → "Ohhhhhh, I'm sorry, but it looks like the magic has worn off! Well, [he/she] gave it [his/her] best shot, folks. Come back whenever you're ready to take another shot at... <Dum-dum-dum>...The Gauuuntlet of Fooortitude!"
 29: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x008C [0x01] GOTO 0x008F

SUBROUTINE_008F:
 31: 0x008F [0x21] END_EVENT
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0090 [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Stooge Moogle (ID: 17437015/0x010A1157), tag_num=0x04)
     0x0097 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
     0x0099 [0x00] END_REQSTACK()
```
