# 16908423 - Airship Door

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Sealion's Den (ID: 32) |
| Block Size       | 216 bytes              |
| Total Events     | 3                      |
| References Count | 12                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [32003](#event-32003) | 0x0001       |      1 |              1 |
| [9](#event-9)         | 0x0002       |    137 |             20 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1EED      |        7917 |
|       1 | 0x0002      |           2 |
|       2 | 0x0000      |           0 |
|       3 | 0x9C3CF     |      639951 |
|       4 | 0xFFFCE129  |  4294762793 |
|       5 | 0xFFFEE94D  |  4294895949 |
|       6 | 0x0C3F      |        3135 |
|       7 | 0x0001      |           1 |
|       8 | 0x9575C     |      612188 |
|       9 | 0xBCA60     |      772704 |
|      10 | 0x206D1     |      132817 |
|      11 | 0x0C01      |        3073 |

## String References

- **7917**: What to do... [Move to the[ armada/ next] warship./Return to Tavnazia./Nothing.]

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

### Event 32003

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 137 bytes |
| Instructions | 20        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 42 24 00 80  01 80 02 80 25 02 00 10     .B$......%...
0010: 02 80 00 4B 00 47 00 03  80 04 80 05 80 06 80 47  ...K.G.........G
0020: 01 2D F8 FF FF 7F F8 FF  FF 7F 31 65 6E 64 2D F8  .-........1end-.
0030: FF FF 7F F8 FF FF 7F 32  65 6E 64 2D F8 FF FF 7F  .......2end-....
0040: F8 FF FF 7F 33 65 6E 64  01 89 00 02 00 10 07 80  ....3end........
0050: 00 89 00 47 00 08 80 09  80 0A 80 0B 80 47 01 2D  ...G.........G.-
0060: F8 FF FF 7F F8 FF FF 7F  31 65 6E 64 2D F8 FF FF  ........1end-...
0070: 7F F8 FF FF 7F 32 65 6E  64 2D F8 FF FF 7F F8 FF  .....2end-......
0080: FF 7F 33 65 6E 64 01 89  00 21 00                 ..3end...!.     
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0005 [0x24] CREATE_DIALOG(message_id=7917*, default_option=2*, option_flags=0*)
    → "What to do... [Move to the[ armada/ next] warship./Return to Tavnazia./Nothing.]"
  3: 0x000C [0x25] WAIT_DIALOG_SELECT()
  4: 0x000D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004B
  5: 0x0015 [0x47] UPDATE_PLAYER_POS(639.951*, -204.503*, -71.347*, yaw=275.5°*)
  6: 0x001F [0x47] WAIT_PLAYER_POS_UPDATE
  7: 0x0021 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1end" with entities [EventEntity, EventEntity]
  8: 0x002E [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2end" with entities [EventEntity, EventEntity]
  9: 0x003B [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "3end" with entities [EventEntity, EventEntity]
 10: 0x0048 [0x01] GOTO 0x0089
 11: 0x004B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0089
 12: 0x0053 [0x47] UPDATE_PLAYER_POS(612.188*, 772.704*, 132.817*, yaw=270.1°*)
 13: 0x005D [0x47] WAIT_PLAYER_POS_UPDATE
 14: 0x005F [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "1end" with entities [EventEntity, EventEntity]
 15: 0x006C [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "2end" with entities [EventEntity, EventEntity]
 16: 0x0079 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "3end" with entities [EventEntity, EventEntity]
 17: 0x0086 [0x01] GOTO 0x0089

SUBROUTINE_0089:
 18: 0x0089 [0x21] END_EVENT
 19: 0x008A [0x00] END_REQSTACK()
```
