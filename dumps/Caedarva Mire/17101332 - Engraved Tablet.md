# 17101332 - Engraved Tablet

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Caedarva Mire (ID: 79) |
| Block Size       | 128 bytes              |
| Total Events     | 2                      |
| References Count | 7                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [305](#event-305)     | 0x0001       |     72 |             18 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F83      |        8067 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0xB9E03     |      761347 |
|       4 | 0x9DA4B     |      645707 |
|       5 | 0xFFFFDFE4  |  4294959076 |
|       6 | 0x02FB      |         763 |

## String References

- **8067**: Place your hand on the tablet? [Yes./No.]

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

### Event 305

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 72 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  02 80 25 02 00 10 02 80    .$......%.....
0010: 00 3A 00 42 43 00 43 01  03 01 10 01 80 29 01 F0  .:.BC.C......)..
0020: FF FF 7F 04 47 00 03 80  04 80 05 80 06 80 47 01  ....G.........G.
0030: 29 01 F0 FF FF 7F 05 01  45 00 02 00 10 01 80 00  ).......E.......
0040: 45 00 01 45 00 20 00 21  00                       E..E. .!.       
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=8067*, default_option=1*, option_flags=0*)
    → "Place your hand on the tablet? [Yes./No.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003A
  4: 0x0013 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0014 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0016 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0018 [0x03] Work_Zone[1] = 1*
  8: 0x001D [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x04)
  9: 0x0024 [0x47] UPDATE_PLAYER_POS(761.347*, 645.707*, -8.220*, yaw=67.1°*)
 10: 0x002E [0x47] WAIT_PLAYER_POS_UPDATE
 11: 0x0030 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x05)
 12: 0x0037 [0x01] GOTO 0x0045
 13: 0x003A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0045
 14: 0x0042 [0x01] GOTO 0x0045

SUBROUTINE_0045:
 15: 0x0045 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x0047 [0x21] END_EVENT
 17: 0x0048 [0x00] END_REQSTACK()
```
