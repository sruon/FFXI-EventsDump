# 17281588 - Blue Rafflesia

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Yuhtunga Jungle (ID: 123) |
| Block Size       | 176 bytes                 |
| Total Events     | 3                         |
| References Count | 5                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [23](#event-23)       | 0x0001       |     62 |             15 |
| [26](#event-26)       | 0x003F       |     62 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1DFC      |        7676 |
|       1 | 0x1DFD      |        7677 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x0002      |           2 |

## String References

- **7676**: A large flower is blooming. You can see something inside it...
- **7677**: Look inside the flower? [Yes./No.]

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

### Event 23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 62 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 24 01 80  02 80 02 80 25 02 00 10   H..#$......%...
0010: 02 80 00 2B 00 42 03 01  10 03 80 2D F8 FF FF 7F  ...+.B.....-....
0020: F8 FF FF 7F 72 61 66 33  01 3B 00 02 00 10 03 80  ....raf3.;......
0030: 00 3B 00 03 01 10 04 80  01 3B 00 20 00 21 00     .;.......;. .!. 
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7676*]:
    → "A large flower is blooming. You can see something inside it..."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x24] CREATE_DIALOG(message_id=7677*, default_option=0*, option_flags=0*)
    → "Look inside the flower? [Yes./No.]"
  3: 0x000C [0x25] WAIT_DIALOG_SELECT()
  4: 0x000D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x002B
  5: 0x0015 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  6: 0x0016 [0x03] Work_Zone[1] = 1*
  7: 0x001B [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "raf3" with entities [EventEntity, EventEntity]
  8: 0x0028 [0x01] GOTO 0x003B
  9: 0x002B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x003B
 10: 0x0033 [0x03] Work_Zone[1] = 2*
 11: 0x0038 [0x01] GOTO 0x003B

SUBROUTINE_003B:
 12: 0x003B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x003D [0x21] END_EVENT
 14: 0x003E [0x00] END_REQSTACK()
```

### Event 26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 62 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               48                 H
0040: 00 80 23 24 01 80 02 80  02 80 25 02 00 10 02 80  ..#$......%.....
0050: 00 69 00 42 03 01 10 03  80 2D F8 FF FF 7F F8 FF  .i.B.....-......
0060: FF 7F 72 61 66 33 01 79  00 02 00 10 03 80 00 79  ..raf3.y.......y
0070: 00 03 01 10 04 80 01 79  00 20 00 21 00           .......y. .!.   
```

#### Opcodes

```
  0: 0x003F [0x48] [System] [7676*]:
    → "A large flower is blooming. You can see something inside it..."
  1: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0043 [0x24] CREATE_DIALOG(message_id=7677*, default_option=0*, option_flags=0*)
    → "Look inside the flower? [Yes./No.]"
  3: 0x004A [0x25] WAIT_DIALOG_SELECT()
  4: 0x004B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0069
  5: 0x0053 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  6: 0x0054 [0x03] Work_Zone[1] = 1*
  7: 0x0059 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "raf3" with entities [EventEntity, EventEntity]
  8: 0x0066 [0x01] GOTO 0x0079
  9: 0x0069 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0079
 10: 0x0071 [0x03] Work_Zone[1] = 2*
 11: 0x0076 [0x01] GOTO 0x0079

SUBROUTINE_0079:
 12: 0x0079 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x007B [0x21] END_EVENT
 14: 0x007C [0x00] END_REQSTACK()
```
