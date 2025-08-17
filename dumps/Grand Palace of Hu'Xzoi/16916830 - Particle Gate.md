# 16916830 - Particle Gate

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Grand Palace of Hu'Xzoi (ID: 34) |
| Block Size       | 136 bytes                        |
| Total Events     | 2                                |
| References Count | 7                                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [172](#event-172)     | 0x0001       |     83 |             22 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C5F      |        7263 |
|       1 | 0x1C60      |        7264 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |
|       4 | 0xFFF8A298  |  4294484632 |
|       5 | 0x3F79A     |      259994 |
|       6 | 0x0800      |        2048 |

## String References

- **7263**: You feel a mysterious energy emanating from the glowing stone in the center of the portal.
- **7264**: Investigate the portal? [Yes./No.]

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

### Event 172

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 83 bytes |
| Instructions | 22       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 20 01 48 00 80  23 24 01 80 02 80 03 80    . .H..#$......
0010: 25 02 00 10 03 80 00 40  00 42 43 00 43 01 03 01  %......@.BC.C...
0020: 10 02 80 29 01 F0 FF FF  7F 18 47 00 04 80 05 80  ...)......G.....
0030: 03 80 06 80 47 01 29 01  F0 FF FF 7F 19 01 50 00  ....G.).......P.
0040: 02 00 10 02 80 00 50 00  03 01 10 03 80 01 50 00  ......P.......P.
0050: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0005 [0x48] [System] [7263*]:
    → "You feel a mysterious energy emanating from the glowing stone in the center of the portal."
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x24] CREATE_DIALOG(message_id=7264*, default_option=1*, option_flags=0*)
    → "Investigate the portal? [Yes./No.]"
  5: 0x0010 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0011 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0040
  7: 0x0019 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x001A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  9: 0x001C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 10: 0x001E [0x03] Work_Zone[1] = 1*
 11: 0x0023 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x18)
 12: 0x002A [0x47] UPDATE_PLAYER_POS(-482.664*, 259.994*, 0.000*, yaw=180.0°*)
 13: 0x0034 [0x47] WAIT_PLAYER_POS_UPDATE
 14: 0x0036 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x19)
 15: 0x003D [0x01] GOTO 0x0050
 16: 0x0040 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0050
 17: 0x0048 [0x03] Work_Zone[1] = 0*
 18: 0x004D [0x01] GOTO 0x0050

SUBROUTINE_0050:
 19: 0x0050 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 20: 0x0052 [0x21] END_EVENT
 21: 0x0053 [0x00] END_REQSTACK()
```
