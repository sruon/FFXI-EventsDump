# 17232303 - Lonely Evergreen

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Beaucedine Glacier (ID: 111) |
| Block Size       | 412 bytes                    |
| Total Events     | 5                            |
| References Count | 17                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [501](#event-501)     | 0x0001       |     41 |             12 |
| [502](#event-502)     | 0x002A       |     83 |             22 |
| [503](#event-503)     | 0x007D       |     55 |             16 |
| [504](#event-504)     | 0x00B4       |    127 |             32 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CF0      |        7408 |
|       1 | 0x1CEC      |        7404 |
|       2 | 0x1CED      |        7405 |
|       3 | 0x1CEE      |        7406 |
|       4 | 0x1CEF      |        7407 |
|       5 | 0x1CE8      |        7400 |
|       6 | 0x1CE9      |        7401 |
|       7 | 0x1CEA      |        7402 |
|       8 | 0x1CEB      |        7403 |
|       9 | 0x1CE3      |        7395 |
|      10 | 0x1CE4      |        7396 |
|      11 | 0x1CE5      |        7397 |
|      12 | 0x0000      |           0 |
|      13 | 0x1CE7      |        7399 |
|      14 | 0x0001      |           1 |
|      15 | 0x1CE6      |        7398 |
|      16 | 0x0002      |           2 |

## String References

- **7397**: So what do you say, kupo!? [Sure, I'll play./No thanks, kupo.]

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

### Event 501

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 41 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 43 00 43 01 03 00  00 02 10 20 01 29 80 AE   BC.C...... .)..
0010: F1 06 01 01 03 03 10 00  00 2B AE F1 06 01 00 80  .........+......
0020: 23 29 80 AE F1 06 01 02  21 00                    #)......!.      
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  2: 0x0004 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  3: 0x0006 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  4: 0x000B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  5: 0x000D [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Stooge Moogle (ID: 17232302/0x0106F1AE), tag_num=0x01)
  6: 0x0014 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[0]
  7: 0x0019 [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7408*]:
    → "Where are the prizes I promised, you say? Why, just bring that $3 to my associate in Xarcabard for the next exciting event, and they're as good as yours! Good luck...you'll need it, kupo!"
  8: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0021 [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Stooge Moogle (ID: 17232302/0x0106F1AE), tag_num=0x02)
 10: 0x0028 [0x21] END_EVENT
 11: 0x0029 [0x00] END_REQSTACK()
```

### Event 502

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 83 bytes |
| Instructions | 22       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                03 01 00 02 10 03            ......
0030: 02 00 03 10 20 01 42 43  00 43 01 29 80 AE F1 06  .... .BC.C.)....
0040: 01 01 03 02 10 01 00 03  03 10 02 00 2B AE F1 06  ............+...
0050: 01 01 80 23 2B AE F1 06  01 02 80 23 2B AE F1 06  ...#+......#+...
0060: 01 03 80 23 2B AE F1 06  01 04 80 23 2B AE F1 06  ...#+......#+...
0070: 01 00 80 23 29 80 AE F1  06 01 02 21 00           ...#)......!.   
```

#### Opcodes

```
  0: 0x002A [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[2]
  1: 0x002F [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[3]
  2: 0x0034 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x0036 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x0037 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  5: 0x0039 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  6: 0x003B [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Stooge Moogle (ID: 17232302/0x0106F1AE), tag_num=0x01)
  7: 0x0042 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
  8: 0x0047 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[2]
  9: 0x004C [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7404*]:
    → "Could it be? Why yes, ladies and gentlemoogles, it looks like [he's/she's] done it! One $3 acquired!"
 10: 0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0054 [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7405*]:
    → "What's that? Why do we need explosives, you say?"
 12: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x005C [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7406*]:
    → "Wh-why, uh...no particular reason at all, kupo! It's just for the...ah...yes, the closing ceremony fireworks, of course! Why, it's a Mog Festival tradition, you know!"
 14: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0064 [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7407*]:
    → "Anyway, I'll just be taking that $3, thankyouverymuch! And here's your reward: $6, kupo! Let's give [him/her] a big round of applause, folks!"
 16: 0x006B [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x006C [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7408*]:
    → "Where are the prizes I promised, you say? Why, just bring that $3 to my associate in Xarcabard for the next exciting event, and they're as good as yours! Good luck...you'll need it, kupo!"
 18: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0074 [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Stooge Moogle (ID: 17232302/0x0106F1AE), tag_num=0x02)
 20: 0x007B [0x21] END_EVENT
 21: 0x007C [0x00] END_REQSTACK()
```

### Event 503

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 55 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         20 01 42                .B
0080: 43 00 43 01 29 80 AE F1  06 01 01 2B AE F1 06 01  C.C.)......+....
0090: 05 80 23 2B AE F1 06 01  06 80 23 2B AE F1 06 01  ..#+......#+....
00A0: 07 80 23 2B AE F1 06 01  08 80 23 29 80 AE F1 06  ..#+......#)....
00B0: 01 02 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x007D [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x007F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0080 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x0082 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x0084 [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Stooge Moogle (ID: 17232302/0x0106F1AE), tag_num=0x01)
  5: 0x008B [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7400*]:
    → "First you'll have to speak with my Gobbie associate stationed just outside the tower southeast of here."
  6: 0x0092 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0093 [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7401*]:
    → "He'll tell you all you need to know, kupo!"
  8: 0x009A [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x009B [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7402*]:
    → "Successfully snag the contents of the casket and bring it back to me, and spoils most spectacular await you!"
 10: 0x00A2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00A3 [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7403*]:
    → "We're all cheering for you, so give it your best shot, kupo!"
 12: 0x00AA [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00AB [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Stooge Moogle (ID: 17232302/0x0106F1AE), tag_num=0x02)
 14: 0x00B2 [0x21] END_EVENT
 15: 0x00B3 [0x00] END_REQSTACK()
```

### Event 504

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00B4    |
| Data Size    | 127 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             20 01 42 43  00 43 01 29 80 AE F1 06       .BC.C.)....
00C0: 01 01 2B AE F1 06 01 09  80 23 2B AE F1 06 01 0A  ..+......#+.....
00D0: 80 23 24 0B 80 0C 80 0C  80 25 02 00 10 0C 80 00  .#$......%......
00E0: 12 01 2B AE F1 06 01 0D  80 23 2B AE F1 06 01 05  ..+......#+.....
00F0: 80 23 2B AE F1 06 01 06  80 23 2B AE F1 06 01 07  .#+......#+.....
0100: 80 23 2B AE F1 06 01 08  80 23 03 01 10 0E 80 01  .#+......#......
0110: 2A 01 02 00 10 0E 80 00  2A 01 2B AE F1 06 01 0F  *.......*.+.....
0120: 80 23 03 01 10 10 80 01  2A 01 29 80 AE F1 06 01  .#......*.).....
0130: 02 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x00B4 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00B6 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00B7 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x00B9 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x00BB [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Stooge Moogle (ID: 17232302/0x0106F1AE), tag_num=0x01)
  5: 0x00C2 [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7395*]:
    → "Welcome, friend, to the Elemental Casket of Mystique and Mystery, kupo! "The what?", you say? I thought you'd never ask!"
  6: 0x00C9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00CA [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7396*]:
    → "Why, it's a riveting and remarkably rewarding game in which you can procure precious prizes simply by surmising a single number!"
  8: 0x00D1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00D2 [0x24] CREATE_DIALOG(message_id=7397*, default_option=0*, option_flags=0*)
    → "So what do you say, kupo!? [Sure, I'll play./No thanks, kupo.]"
 10: 0x00D9 [0x25] WAIT_DIALOG_SELECT()
 11: 0x00DA [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0112
 12: 0x00E2 [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7399*]:
    → "That's the spirit, kupo!"
 13: 0x00E9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x00EA [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7400*]:
    → "First you'll have to speak with my Gobbie associate stationed just outside the tower southeast of here."
 15: 0x00F1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x00F2 [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7401*]:
    → "He'll tell you all you need to know, kupo!"
 17: 0x00F9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x00FA [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7402*]:
    → "Successfully snag the contents of the casket and bring it back to me, and spoils most spectacular await you!"
 19: 0x0101 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x0102 [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7403*]:
    → "We're all cheering for you, so give it your best shot, kupo!"
 21: 0x0109 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x010A [0x03] Work_Zone[1] = 1*
 23: 0x010F [0x01] GOTO 0x012A
 24: 0x0112 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x012A
 25: 0x011A [0x2B] Stooge Moogle (ID: 17232302/0x0106F1AE) [7398*]:
    → "Awww...what a spoilsport, kupo! This festival won't be around forever, so come back soon if you change your mind!"
 26: 0x0121 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0122 [0x03] Work_Zone[1] = 2*
 28: 0x0127 [0x01] GOTO 0x012A

SUBROUTINE_012A:
 29: 0x012A [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Stooge Moogle (ID: 17232302/0x0106F1AE), tag_num=0x02)
 30: 0x0131 [0x21] END_EVENT
 31: 0x0132 [0x00] END_REQSTACK()
```
