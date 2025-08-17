# 16912907 - Auroral Updraft

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al'Taieu (ID: 33) |
| Block Size       | 92 bytes          |
| Total Events     | 2                 |
| References Count | 3                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [157](#event-157)     | 0x0001       |     53 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CA2      |        7330 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |

## String References

- **7330**: Return to the palace entrance? [Yes./No.]

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

### Event 157

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 53 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  02 80 25 02 00 10 02 80    .$......%.....
0010: 00 27 00 42 43 00 43 01  03 01 10 01 80 29 01 F0  .'.BC.C......)..
0020: FF FF 7F 09 01 32 00 02  00 10 01 80 00 32 00 01  .....2.......2..
0030: 32 00 20 00 21 00                                 2. .!.          
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=7330*, default_option=1*, option_flags=0*)
    → "Return to the palace entrance? [Yes./No.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0027
  4: 0x0013 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0014 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0016 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0018 [0x03] Work_Zone[1] = 1*
  8: 0x001D [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x09)
  9: 0x0024 [0x01] GOTO 0x0032
 10: 0x0027 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0032
 11: 0x002F [0x01] GOTO 0x0032

SUBROUTINE_0032:
 12: 0x0032 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x0034 [0x21] END_EVENT
 14: 0x0035 [0x00] END_REQSTACK()
```
