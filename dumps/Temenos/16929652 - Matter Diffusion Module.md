# 16929652 - Matter Diffusion Module

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Temenos (ID: 37) |
| Block Size       | 156 bytes        |
| Total Events     | 2                |
| References Count | 7                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1026](#event-1026)   | 0x0001       |    103 |             24 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C42      |        7234 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x0064      |         100 |
|       4 | 0x8D9A0     |      580000 |
|       5 | 0x14FF0     |       86000 |
|       6 | 0x0400      |        1024 |

## String References

- **7234**: Returning to entrance. [Sure./No thanks.]

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

### Event 1026

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 103 bytes |
| Instructions | 24        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  01 80 25 02 00 10 01 80    .$......%.....
0010: 00 1B 00 03 01 10 02 80  01 2B 00 02 00 10 02 80  .........+......
0020: 00 2B 00 03 01 10 01 80  01 2B 00 02 01 10 01 80  .+.......+......
0030: 00 36 00 01 64 00 42 03  00 00 01 10 03 01 10 03  .6..d.B.........
0040: 80 43 00 43 01 03 01 10  00 00 29 01 F0 FF FF 7F  .C.C......).....
0050: 02 47 00 04 80 05 80 01  80 06 80 47 01 29 01 F0  .G.........G.)..
0060: FF FF 7F 03 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=7234*, default_option=0*, option_flags=0*)
    → "Returning to entrance. [Sure./No thanks.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001B
  4: 0x0013 [0x03] Work_Zone[1] = 1*
  5: 0x0018 [0x01] GOTO 0x002B
  6: 0x001B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x002B
  7: 0x0023 [0x03] Work_Zone[1] = 0*
  8: 0x0028 [0x01] GOTO 0x002B

SUBROUTINE_002B:
  9: 0x002B [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x0036
 10: 0x0033 [0x01] GOTO 0x0064
 11: 0x0036 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 12: 0x0037 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[1]
 13: 0x003C [0x03] Work_Zone[1] = 100*
 14: 0x0041 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 15: 0x0043 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 16: 0x0045 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[0]
 17: 0x004A [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x02)
 18: 0x0051 [0x47] UPDATE_PLAYER_POS(580.000*, 86.000*, 0.000*, yaw=90.0°*)
 19: 0x005B [0x47] WAIT_PLAYER_POS_UPDATE
 20: 0x005D [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)

SUBROUTINE_0064:
 21: 0x0064 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 22: 0x0066 [0x21] END_EVENT
 23: 0x0067 [0x00] END_REQSTACK()
```
