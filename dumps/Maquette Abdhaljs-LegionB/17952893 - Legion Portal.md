# 17952893 - Legion Portal

## Common Data

| Field            | Value                               |
|------------------|-------------------------------------|
| Zone             | Maquette Abdhaljs-LegionB (ID: 287) |
| Block Size       | 124 bytes                           |
| Total Events     | 2                                   |
| References Count | 6                                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [10004](#event-10004) | 0x0001       |     72 |             16 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1BA3      |        7075 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x03E7      |         999 |
|       4 | 0x0078      |         120 |
|       5 | 0x40000000  |  1073741824 |

## String References

- **7075**: Exit the maquette? [Yes, exit./No, remain.]

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

### Event 10004

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 72 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 24 00  80 01 80 02 80 25 02 00   .....$......%..
0010: 10 02 80 00 37 00 42 03  01 10 03 80 43 00 43 01  ....7.B.....C.C.
0020: 62 01 80 F0 FF FF 7F F0  FF FF 7F 6D 61 69 6E 02  b..........main.
0030: 80 1C 04 80 01 47 00 02  00 10 01 80 00 47 00 03  .....G.......G..
0040: 01 10 05 80 01 47 00 21  00                       .....G.!.       
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x24] CREATE_DIALOG(message_id=7075*, default_option=1*, option_flags=0*)
    → "Exit the maquette? [Yes, exit./No, remain.]"
  2: 0x000D [0x25] WAIT_DIALOG_SELECT()
  3: 0x000E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0037
  4: 0x0016 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0017 [0x03] Work_Zone[1] = 999*
  6: 0x001C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x001E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x0020 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  9: 0x0031 [0x1C] WAIT(120* ticks)
 10: 0x0034 [0x01] GOTO 0x0047
 11: 0x0037 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0047
 12: 0x003F [0x03] Work_Zone[1] = 1073741824*
 13: 0x0044 [0x01] GOTO 0x0047

SUBROUTINE_0047:
 14: 0x0047 [0x21] END_EVENT
 15: 0x0048 [0x00] END_REQSTACK()
```
