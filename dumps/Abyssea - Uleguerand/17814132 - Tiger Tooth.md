# 17814132 - Tiger Tooth

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 60 bytes                       |
| Total Events     | 2                              |
| References Count | 2                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [361](#event-361)     | 0x0001       |     25 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0020      |          32 |
|       1 | 0x1FA2      |        8098 |

## String References

- **8098**: I had occasion to receive trainin' from old Maat just once. Don't remember how many years ago it was, but I've still got the bruises t' show for it. Ahahaha!

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

### Event 361

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 25 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  6E 74 D2 0F 01 00 80 99   .....opnt......
0010: 74 D2 0F 01 1D 01 80 23  21 00                    t......#!.      
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x6E] Tiger Tooth (ID: 17814132/0x010FD274) uses emote 32*
  4: 0x000F [0x99] Wait for Tiger Tooth (ID: 17814132/0x010FD274) animation to complete
  5: 0x0014 [0x1D] PRINT_EVENT_MESSAGE(message_id=8098*)
    → "I had occasion to receive trainin' from old Maat just once. Don't remember how many years ago it was, but I've still got the bruises t' show for it. Ahahaha!"
  6: 0x0017 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0018 [0x21] END_EVENT
  8: 0x0019 [0x00] END_REQSTACK()
```
