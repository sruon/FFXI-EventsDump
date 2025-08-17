# 16974310 - Djinabaha

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al Zahbi (ID: 48) |
| Block Size       | 92 bytes          |
| Total Events     | 2                 |
| References Count | 3                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [209](#event-209)     | 0x0001       |     52 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x1DFD      |        7677 |
|       2 | 0x0000      |           0 |

## String References

- **7677**: I was beginning to think the auction house was going to have to shut down for good...until you saved me. Please accept my thanks.

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

### Event 209

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 52 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    43 00 43 01 20 01 42  03 01 10 00 80 1E F0 FF   C.C. .B........
0010: FF 7F 6F 70 1D 01 80 66  02 80 F8 FF FF 7F F8 FF  ..op...f........
0020: FF 7F 70 61 73 30 53 F8  FF FF 7F F8 FF FF 7F 70  ..pas0S........p
0030: 61 73 30 21 00                                    as0!.           
```

#### Opcodes

```
  0: 0x0001 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  1: 0x0003 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  2: 0x0005 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x0007 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x0008 [0x03] Work_Zone[1] = 1*
  5: 0x000D [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x0012 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0013 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x0014 [0x1D] PRINT_EVENT_MESSAGE(message_id=7677*)
    → "I was beginning to think the auction house was going to have to shut down for good...until you saved me. Please accept my thanks."
  9: 0x0017 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=0*
 10: 0x0026 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 11: 0x0033 [0x21] END_EVENT
 12: 0x0034 [0x00] END_REQSTACK()
```
