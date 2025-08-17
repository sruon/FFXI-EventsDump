# 16957467 - Pursuivant

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Abdhaljs Isle-Purgonorgo (ID: 44) |
| Block Size       | 100 bytes                         |
| Total Events     | 2                                 |
| References Count | 5                                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [3](#event-3)         | 0x0001       |     55 |             17 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CA4      |        7332 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x007A      |         122 |
|       4 | 0x00E6      |         230 |

## String References

- **7332**: Teleport to [Upper Jeuno/Aht Urhgan Whitegate/Northern San d'Oria/3/Port Bastok/5/Windurst Waters]? [Yes./No.]

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

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 55 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 1E F0 FF FF 7F  6F 70 24 00 80 01 80 02    ......op$.....
0010: 80 25 02 00 10 02 80 00  36 00 42 03 01 10 01 80  .%......6.B.....
0020: 73 03 80 F8 FF FF 7F F0  FF FF 7F 1C 04 80 43 00  s.............C.
0030: 43 01 30 01 36 00 21 00                           C.0.6.!.        
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0008 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0009 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x000A [0x24] CREATE_DIALOG(message_id=7332*, default_option=1*, option_flags=0*)
    → "Teleport to [Upper Jeuno/Aht Urhgan Whitegate/Northern San d'Oria/3/Port Bastok/5/Windurst Waters]? [Yes./No.]"
  5: 0x0011 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0012 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0036
  7: 0x001A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  8: 0x001B [0x03] Work_Zone[1] = 1*
  9: 0x0020 [0x73] EventEntity casts magic 122* on LocalPlayer
 10: 0x002B [0x1C] WAIT(230* ticks)
 11: 0x002E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 12: 0x0030 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 13: 0x0032 [0x30] SET_UCOFF_CONTINUE_ZERO()
 14: 0x0033 [0x01] GOTO 0x0036

SUBROUTINE_0036:
 15: 0x0036 [0x21] END_EVENT
 16: 0x0037 [0x00] END_REQSTACK()
```
